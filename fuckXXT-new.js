// ==UserScript==
// @name         fuckXXT.insideAI-copy
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  try to take over the world!
// @author       You
// @match        https://*/*
// @match        https://mooc1.chaoxing.com/mooc-ans/mooc2/*
// @match        https://mooc1.chaoxing.com/mycourse/studentstudy?chapterId=*&courseId=*
// @icon         data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA5RJREFUWEftlluoVVUUhr/z4IHIwBfFykgTQkQyMMK0pJv4YIWXSsoHBSvNS0WKcUSwIEWwlEjBEEUU0bzkQ5EP3hMqK/GGZRJiN8METRRUFHR+Mlass85Ze6/ty0FwwOJc5hxz/PMfY/xjNtHB1tTB8bmlATQD9wB3A6eBE8DVRhltlAGDvQKMBB4vBLuS1n4Fvk+gPgN+yq13AgYDPeI7BfwBbG8EwPvA63HrfOyDwF3AAwVAnwO/AENSoCcAQRStpSqA9cBL4b0f+AbYm1jYFvS71AXoC4wD3ihJxRbgh2DhKaC5CoBrucNmp9t+DFyKNAwHBgLnAH//L/YOAN7LgX4XWJQ7ZwywDvitHgBv+Wg4ejsplYl3gEGFWz4C7Cv8L8+c+7+Lov0SEOSntQDMBWbFgeZxTwT3UO0YsDaqX1p/LqF9MzAC+Au4LxXjVuBZ4Kg/ywD0i2q+MzktT86vAW8Bn0SQacAy4HKFtnsYMPfdgQ25tIwCNpcBWADMCMqk7pkoOOM9D3xVIXB+iynL18DLAaZUCXcCTwKToqdtwTkpb+buhQaDS/caoFv4/R/cv8sYyCrfAvwxHAW0q8Hgps5U5W0CsCL7R3sAVKs/Q1bvSMUl4n8AWWnELGALWfvWfAOm1m9mLQCPhYNS6q0vAL8DPStGV2DUgGGx/81UgEujEwTxdWjGjeX2GLDPbTXp9rCxSdlOVmDAHBtY0dFkzHrxAprq6IzYBLxYxkAW3PXDwEMVb+2MsGseTCAuAh8mmZ1X8JWFicBiwDZuw0A+eLZuDztsyuzVNAum5FTRLjG4wlS03TGYDC6IVgD6RJ/fC6wO0RiaUvRB2mULFk1lmwy4R1OyFaxixef9/gW6Ar1CPVsB+CKGi3l7GpiqTif1OxNzXNnUWZb8LE7NQnXfqhosuVSqIxZh/1ShByJ3Uq7Gaz4Y1O4lIbmjgftjzfowx060eibYrIXbqKgApgMfAYeAt+NxoW6bDtUvb754TItDqKplouYcUFNamQCeC4mtdaDvPQOvrBo1sdaS64QjgAOujWU6YK8rm4qQY1MllBHnt4IyPjwVkfkxmsuw9AYW5mbG3/ECand/vQdJ5mS+vVFmTkNZOR4PUV/H1pI15Nc5Nqp8jt1SqwrAA3xYWiMWYz2zgAWt8tW0RgBkB5kmq9nq9pnu7c+HXJvrjUlwdiSwZ+sFd/1mAFQ5t/Ke2wA6nIHr54C0BK9FxloAAAAASUVORK5CYII=
// @grant        GM_xmlhttpRequest
// ==/UserScript==
//推广，兼容，内置后端，优化题目信息结构,题目记忆功能，题库法，启停，拖动


(function() {
    'use strict';
    //设置参数
    var index = 0//从第一题开始
    var num = 5 //每次最多5题


    //控制面板
    const panel = document.createElement("div");
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

    if (window.top === window.self) {
        document.body.appendChild(panel);
    }
    panel.appendChild(btn1)
    panel.appendChild(btn2)
    panel.appendChild(btn3)
    panel.appendChild(btn4)
    //--------------------------------------------------------------------------


    //xxt获取题目与选项
    var getsubject =function(){
        var subject = []
        var qus = document.querySelectorAll(".padBom50.questionLi.fontLabel.singleQuesId");
        qus.forEach(function (item) {
            var qusname = item.querySelector(".mark_name.colorDeep.fontLabel.workTextWrap")?.childNodes[1]?.textContent +
                item.querySelector(".mark_name.colorDeep.fontLabel.workTextWrap")?.childNodes[2]?.textContent.slice(0,-8);
            var optElements = item.querySelectorAll('.fl.answer_p');
            var optnamels = Array.from(optElements).map(opt => opt.parentNode.childNodes[1].textContent+':'+opt.textContent);
            subject.push('题目:'+qusname+'。选项:'+optnamels.join(","));
        });
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
        const ls = JSON.parse(response.responseText);
        console.log(ls)
        for (let j =0; j < ls.length; j++) {
            for (let k=0; k<ls[j].length;k++){
                var choice = ls[j][k].charCodeAt(0) - 65;
                document.querySelectorAll(".stem_answer")[j+index].querySelectorAll("span")[choice].click()
            }
        }
    }

    //接口solve
    var solve = function(subject) {
        return new Promise((resolve, reject) => {
            GM_xmlhttpRequest({
                method: 'POST',
                url: 'http://localhost:5000/solve',
                headers: { 'Content-Type': 'application/json' },
                data: JSON.stringify( subject ),
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
        index=0
        clear()//初始化
        var subjects = getsubject()//获取题目
        while (index < subjects.length) {
            await solve(subjects.slice(index, index + num)) // 等待当前批次完成
            index += num
            //break调试点
        }
        //document.querySelector(".sub-button").childNodes[1].click()//暂存
    }
    //-------------------------------------------------------------------------------------


    //xxt导出题目为csv格式
    var subexp = function(){
        var csvls = []
        var div = document.querySelectorAll(".aiAreaContent")
        div.forEach(function (div) {
            var sub = ""
            var ans = ""
            var ls =div.querySelectorAll(".workTextWrap")
            ls.forEach(function(ls){
                sub+=ls.textContent + "<br>"
            })
            ans=div.querySelector(".colorDeep.marginRight40.fl").textContent.slice(-1)
            csvls。push(`"${sub}","${ans}"`)
        });
        console.log(csvls)
        return(csvls)
    }

    //xxt下载csv文件
    var creatCSV = function(csvls){
        var csv = csvls.join("\n")
        const blob = new Blob(["\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        const url = URL.createObjectURL(blob);
        link.href = url;
        link.download = 'sub.csv';
        link.click();
        URL.revokeObjectURL(url);
    }

    //学习通导出主函数
    var xxtexp = async function(){
        var csvls=subexp()
        creatCSV(csvls)
    }
    //--------------------------------------------------------------------------------------------


    //URL判断
    var url = function(){
        let currentURL = window.location.href;
        if (/^https:\/\/onlineexamh5new\.zhihuishu\.com\/stuExamWeb\.html#.*$/.test(currentURL)){//智慧树
            //btn1.onclick=zhs
            btn1.style.cssText=`
            background-color:white;
            `;
        }else if(/^https:\/\/mooc1\.chaoxing\.com\/mooc-ans\/mooc2\/work\/view?.*$/.test(currentURL)){//学习通view导出
            btn4.onclick=xxtexp
            btn4.style.cssText=`
            background-color:white;
            `;
        }else if(/^https:\/\/mooc1\.chaoxing\.com\/mooc-ans\/mooc2\/work\/dowork?.*$/.test(currentURL)){//学习通dowork作业
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
