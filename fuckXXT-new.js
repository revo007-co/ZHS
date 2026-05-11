// ==UserScript==
// @name         fuckXXT
// @namespace    http://tampermonkey.net/
// @version      2026-05-01
// @description  try to take over the world!
// @author       You
// @match        https://*/*
// @match        https://mooc1.chaoxing.com/mooc-ans/mooc2/*
// @match        https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=*&courseId=*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=chaoxing.com
// @grant        GM_xmlhttpRequest
// ==/UserScript==
//控制面板，推广，脚本间通信，兼容


(function() {
    'use strict';
    //设置参数
    var index = 0//从第一题开始
    var num = 5 //每次最多5题


    //控制面板
    const panel = document.createElement("div");
    panel.id = 'panel';
    panel.style.cssText = `
        position: fixed;
        display : flex;
        align-items: center;
        justify-content: center;
        top: 40px;
        right: 380px;
        width: 300px;
        height: 120px;
        background-color: rgba(51, 53, 54, 0.5);
        z-index: 999999;
        gap:30px;
    `;

    const style = document.createElement('style');
    style.textContent = `
    .btn:hover {
        background-color: #f0f0f0 !important;
        transform: scale(1.1) !important;
        cursor: pointer !important;
    }
    .btn {
     width:40px;
     height:50px;
     background-color:rgba(50,50,50,0.1);
    }
   `;
    document.head.appendChild(style);

    const btn1 =document.createElement("button")
    btn1.className = 'btn';
    btn1.textContent = '作业'
    const btn2 =document.createElement("button")
    btn2.className = 'btn';
    btn2.textContent = '考试'
    const btn3 =document.createElement("button")
    btn3.className = 'btn';
    btn3.textContent = '网课'
    const btn4 =document.createElement("button")
    btn4.className = 'btn';
    btn4.textContent = '导出'

    const targetBody = document.getElementById('body-content');
    if (targetBody) {
        targetBody.appendChild(panel);
    }
    else{
        document.body.appendChild(panel)
    }

    panel.appendChild(btn1)
    panel.appendChild(btn2)
    panel.appendChild(btn3)
    panel.appendChild(btn4)
    //--------------------------------------------------------------------------


    //xxt获取题目与选项
    var getsubject =function(){
        var qusls = [];
        var optls = [];
        var subject = []

        var qus = document.querySelectorAll(".padBom50.questionLi.fontLabel.singleQuesId");
        qus.forEach(function (item) {
            var qusname = item.querySelector(".mark_name.colorDeep.fontLabel.workTextWrap")?.childNodes[1]?.textContent +
                item.querySelector(".mark_name.colorDeep.fontLabel.workTextWrap")?.childNodes[2]?.textContent.slice(0.-8);
            qusls.push(qusname);//已获取题目

            var optElements = item.querySelectorAll('.fl.answer_p');
            var optnamels = Array.from(optElements).map(opt => opt.textContent);
            optls.push(optnamels);//已获取选项
        });

        for (let i = 0; i < qusls.length; i++) {
            subject.push({
                "question": qusls[i],
                "options": optls[i]
            });
        }
        console.log(subject)
        return subject
    }

    //xxt初始化（清空已选答案）
    var clear = function(){
        document.querySelectorAll(".stem_answer").forEach(function (item) {
            item.querySelectorAll("span").forEach(function (item) {
                item.classList.remove("check_answer");
            });
        });
    }

    //xxt答案处理与填充
    var handle = function(response){
        const ls = JSON.parse(JSON.parse(response.responseText));
        console.log(ls)
        for (let j =0; j < ls.length; j++) {
            for (let k=0; k<ls[j].length;k++){
                var choice = ls[j][k].charCodeAt(0) - 65;
                document.querySelectorAll(".stem_answer")[j+index].querySelectorAll("span")[choice].click()
            }
        }
    }

    //接口1
    var solve = function(sub) {
        return new Promise((resolve, reject) => {
            GM_xmlhttpRequest({
                method: 'POST',
                url: 'http://localhost:5000/solve',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify({ subject: sub }),
                onload: function(response) {
                    handle(response)
                    resolve() // 完成一批
                },
                onerror: reject
            });
        });
    }

    //学习通作业主函数
    var xxt =async function(){
        alert("启动")
        clear()//初始化
        var subjects = getsubject()//获取题目
        while (index < subjects.length) {
            await solve(subjects.slice(index, index + num)) // 等待当前批次完成
            index += num
        }
        //document.querySelector(".sub-button").childNodes[1].click()//暂存
    }
    //-------------------------------------------------------------------------------------


    //xxt导出题目
    var subexp = function(){
        var csv = []
        var div = document.querySelectorAll(".aiAreaContent")
        div.forEach(function (div) {
            var sub = ""
            var ans = ""
            var ls =div.querySelectorAll(".workTextWrap")
            ls.forEach(function(ls){
                sub+=ls.textContent + "<br>"
            })
            ans=div.querySelector(".colorDeep.marginRight40.fl").textContent.slice(-1)
            csv.push(`"${sub}","${ans}"`)
        });
        console.log(csv)
        return(csv)
    }
    //接口2
    var csv = function(subs) {
        return new Promise((resolve, reject) => {
            GM_xmlhttpRequest({
                method: 'POST',
                url: 'http://localhost:5000/csv',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify(subs),
                onload: function(res) {
                // 手动触发下载
                const blob = new Blob([res.responseText], { type: 'text/plain' });
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = 'output.csv';
                link.click();
                URL.revokeObjectURL(link.href);
                resolve(res);
            },
                onerror: reject
            });
        });
    }

    //学习通导出主函数
    var xxtexp = async function(){
        var subs=subexp()
        await csv(subs)
    }
    //--------------------------------------------------------------------------------------------


    //URL判断
    var url = function(){
        let currentURL = window.location.href;
        if (/^https:\/\/onlineexamh5new\.zhihuishu\.com\/stuExamWeb\.html#.*$/.test(currentURL)){
            //btn1.onclick=zhs
            btn1.style.cssText=`
            background-color:white;
            `;
        }else if(/^https:\/\/mooc1\.chaoxing\.com\/mooc-ans\/mooc2\/work\/view?.*$/.test(currentURL)){//学习通view
            btn4.onclick=xxtexp
            btn4.style.cssText=`
            background-color:white;
            `;
        }else if(/^https:\/\/mooc1\.chaoxing\.com\/mooc-ans\/mooc2\/work\/dowork?.*$/.test(currentURL)){//学习通dowork
            btn1.onclick=xxt
            btn1.style.cssText=`
            background-color:white;
            `;
        }else{
            console.log('未匹配到有效url')
        }
    }
    window.setTimeout(url,1000)

})();
