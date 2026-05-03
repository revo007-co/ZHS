// ==UserScript==
// @name         fuckXXT
// @namespace    http://tampermonkey.net/
// @version      2026-05-01
// @description  try to take over the world!
// @author       You
// @match        https://mooc1.chaoxing.com/mooc-ans/mooc2/work/dowork?courseId=*&classId=*&cpi=*&workId=*&answerId=*=*&enc=*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=chaoxing.com
// @grant        GM_xmlhttpRequest
// ==/UserScript==
//控制面板，5*n+m，服务端AI多次调用

(function() {
    'use strict';
    //获取题目与选项
    var getsubject =function(){
        var qusls = [];
        var optls = [];
        var subject = []

        var qus = document.querySelectorAll(".padBom50.questionLi.fontLabel.singleQuesId");
        qus.forEach(function (item) {
            var qusname = item.querySelector(".mark_name.colorDeep.fontLabel.workTextWrap")?.childNodes[1]?.textContent +
                item.querySelector(".mark_name.colorDeep.fontLabel.workTextWrap")?.childNodes[2]?.textContent.slice(0, -8);
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

    //初始化（清空已选答案）
    var clear = function(){
        document.querySelectorAll(".stem_answer").forEach(function (item) {
            item.querySelectorAll("span").forEach(function (item) {
                item.classList.remove("check_answer");
            });
        });
    }

    //答案处理与填充
    var handle = function(response){
        const result = JSON.parse(response.responseText);//response.responseText将application/json转为字符串，再用parse解析为'{}'对象
        var ls = JSON.parse(result.answer)//答案列表
            for (let j = 0; j < ls.length; j++) {
                for (let k=0; k<ls[j].length;k++){
                    var choice = ls[j][k].charCodeAt(0) - 65;
                    document.querySelectorAll(".stem_answer")[j].querySelectorAll("span")[choice].click()
                }
            }
        document.querySelector(".sub-button").childNodes[1].click()//暂存
    }

    //主函数
    var main =async function(){
        clear()
        var sub =getsubject()
        try {
            const response = await new Promise((resolve, reject) => {
                GM_xmlhttpRequest({
                    method: 'POST',
                    url: 'http://localhost:5000/solve',
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify({ subject:sub }),
                    onload: resolve,
                    onerror: reject
                });
            });
            handle(response)
        } catch (error) {
            console.error('请求失败:', error);
        }

    }
    window.setTimeout(main,2000)
})();
