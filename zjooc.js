
// ==UserScript==
// @name         revo-ZJOOC-copy自动播放
// @namespace    https://github.com/ColdThunder11/ZJOOCAutoPlay
// @version      0.3
// @description  ZJOOC自动播放下一课，详细使用需求见附加信息或readme.md
// @author       ColdThunder11,00LT00,liudanT800
// @match        *://www.zjooc.cn/ucenter/student/course/study/*/plan/detail/*
// @grant        none
// @supportURL   https://github.com/ColdThunder11/ZJOOCAutoPlay/issues
// ==/UserScript==
//pdf tab纠正 标签页切换后播放 控制面板 DOM刷新检测 检查间隔
// 间隔时间监测到当前课程播放完成后，会执行课程跳转函数，进行tab跳转，此时加载video，然而若加载时，playinterval再次检测，假设尚未加载完成视频的状态下进度条为00:00/00:00，则又会执行
//课程切换函数，即课程进行了连续两次跳转（可能多次）。解决方案1：playinterval延长；2：接收到课程加载完成的信息后，才启用检测函数
//检测函数间隔执行，有不必要的开销，且课程播放完后，最不理想的情况是等待一个playinterval，故需考虑实时接受视频播放完成的信号进行改进，即当视频完成之后，会自动发送信号，但如何实现
//在视频未加载完成时点击播放，可能会出现，视频无法正常接收，此时1.刷新 2.增加视频延迟播放时间

(function () {
    console.log('=== zjooc脚本已启动 ===');
    'use strict';
    var startTime = 2000; // 脚本开始时间（毫秒）
    var checkInterval = 20000; // 检查间隔时间（毫秒）
    var delayInterval = 5000;//视频延迟播放时间
    var jumpInterval = 3000;//视频结束到课程跳转间隔
    var speedIndex = 0; // 播放速度
    var muteFlag = true; // 是否静音


    // 获取所有 role="tab" 的元素，并排除不需要的 tab
    var getTabs = function () {
        var allTabs = document.querySelectorAll('[role="tab"]');
        var filteredTabs = [];

        allTabs.forEach(function (tab, index) {
            // 排除前两个 tab
            if (index >= 2) {
                filteredTabs.push(tab);
            }
        });
        console.log("获取tab中")
        return filteredTabs;
    };

    // 跳转到下一个 tab
    var nextTabFunc = function () {
        console.log("正在跳转tab")
        var tabs = getTabs();
        var currentTab = Array.from(tabs).find(tab => tab.getAttribute('aria-selected') === 'true');
        var currentIndex = tabs.indexOf(currentTab);
        var nextTab = tabs[currentIndex + 1];

        if (nextTab) {
            nextTab.click(); // 点击下一个 tab
            playVideoFunc(); 
        } else {
            // 所有 tab 都已跳转完毕，跳转到下一个课程
            nextVideoFunc();
        }
    };

    // 跳转到下一个课程
    var nextVideoFunc = function () {
        console.log("正在跳转课程")
        var currentClass = document.getElementsByClassName("el-menu-item is-active")[1];/*当前正在播放的课程*/
        var nextClass = currentClass.nextSibling;/*下一个课程*/

        if (nextClass == null) {
            console.log("正在跳转章节")
            currentClass.parentNode.parentNode.nextSibling.childNodes[0].click();/*跳转到下一章后点击展开*/
            nextClass = currentClass.parentNode.parentNode.nextSibling.childNodes[1].childNodes[1];/*获取下一个课程*/
        }

        if (nextClass == null) {
            alert("所有课程已经学习完毕。");
        } else {
            nextClass.click();
            playVideoFunc();
        }
    };
    //视频播放
    var playVideoFunc = function () {
        setTimeout(function () {
        var vid = document.getElementsByTagName("video")[0];
        if (vid) {
            var spd = vid.parentElement.children[8];
            var cbf = vid.parentNode.childNodes[2];
            var playLayerf = cbf.childNodes[0];
            /*速度*/
            spd.children[speedIndex].click();
            /*音量*/
            if (muteFlag) {
                cbf.children[18].click();
            }
            // 绑定完成事件
            playLayerf.click();
            attachVideoEndListener(vid);
        }
        }, delayInterval);
    };
     // 在 playVideoFunc 中绑定事件
     var attachVideoEndListener = function(vid) {
        vid.removeEventListener('ended', onVideoEnd);// 移除旧监听器，避免重复绑定
        vid.addEventListener('ended', onVideoEnd);
     };
     var onVideoEnd = function() {
        console.log("视频播放结束");
         setTimeout(function () {
             nextTabFunc()
         },jumpInterval)
     };

     //标签修正,因网页刷新之后存在，视频标签与左侧标签（会激活第一个标签）不符的现象，导致第一次跳转会到第二个可播放视频
     var correct = function () {
        var li = document.getElementsByClassName("ico")[0].parentNode.childNodes[2].childNodes
        var text = [li[0].innerText, li[2].innerText] /*获取真正的章，节名*/
        var chapters = document.querySelectorAll('[role="menubar"]')[1].childNodes
        for (var item of chapters) {
            var chaptername = item.childNodes[0].childNodes[0].innerText
            if (chaptername == text[0]) {
                var sections = item.childNodes[1].childNodes
                for (var section of sections) {
                    var sectionname = section.innerText
                    if (sectionname == text[1]) {
                        section.childNodes[0].click()
                        return
                    }
                }
                break
            }
        }
    }
     //检查函数
     var detectiveFunc = function () {
          playVideoFunc()//重置播放
          var vid = document.getElementsByTagName("video")[0];
          if (vid) {
            var cb = vid.parentNode.childNodes[2];/*视频总控*/
            var processBar = cb.childNodes[7];/*进度条*/
            var processText = processBar.innerText;
            var pctime = processText.split('/');
            var ctime = pctime[0].trim();
            var etime = pctime[1].trim();

            if (etime=="00:00") {
                location.reload()
            }
        }
     }

    // 主函数
    var ScriptFunc = function () {
        console.log("主函数中")
        correct()
        playVideoFunc();
        window.setInterval(detectiveFunc, checkInterval);
    };
    window.setTimeout(ScriptFunc, startTime);
})();


