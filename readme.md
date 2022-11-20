# 海洋大學 熱音社 搶團系統

## 開發始末

學期初時搶團過程因為有新生｢不知道一次可以搶多團」(個人覺得FB搶團不夠人性化)，以及陳X宇學長之前說過｢在手機12:00上船時發現提早」(各設備時間不一致)，和幹部在搶團後還要手動比對搶團順序(超級浪費時間)等諸多可以自動化的或是靠網路解決的問題，因此開發這網頁協助幹部。


## 網頁介紹

### 主頁
![](https://i.imgur.com/CSHmZhV.jpg)
<div style="color:#eebf34;">黃色部分：選擇時段以及團名</div>
<div style="color:#1ba15e;">綠色部分：目前搶團剩餘時段，若時段已經有人會以紅色底標示(如下圖)</div>
<div style="color:#03245e;">深藍部分：倒數計時器，會以 ??:?? 表示，準確時間到秒，重新整理能與伺服器同步，目前測試下來會比伺服器快0.5秒左右，建議多重新整理確保與伺服器同步</div>
<div style="color:#17a8e0;">天藍色部分：有三種按鍵，分別為Memory、Submit、Clear
<li>Memory：將目前選擇情形作保存，避免重新整理或關閉網頁消失需要重選</li>
<li>Submit：送出時段與團名，若倒數計時器未變成Start!!實會無法傳送</li>
</div>

![](https://i.imgur.com/FQBVrFS.jpg)

### 傳送後頁面

#### 正常頁面
![](https://i.imgur.com/a6G6EFo.jpg)

<div style="display: flex;flex-wrap: wrap;">
    送出後會得到三種結果
    <div style="color:green;">
        Accept,&nbsp
    </div>
    <div style="color:red;">
        Denied, Too Late
    </div>
</div>
<li style="color:green;">Accept：搶團成功</li>
<li style="color:red;">Too Late：手速太慢，被搶走了</li>
<li style="color:red;">Denied：錯誤輸入，可能沒時段選不完整，像是只選星期沒選時間，或只選星期</li>

#### 不正常頁面

![](https://i.imgur.com/NMVPUM1.jpg)
手速太快了，在伺服器開放前就按出submit
<hr>

![](https://i.imgur.com/drPnvmB.jpg)
目前測試到在**未按照順序填寫**時會發生，所以請從第一格照順序填下來

### 管理頁面
![](https://i.imgur.com/pymOnR6.jpg)
在網址加入/login會進入到登入頁面，輸入密碼後會進到管理頁

![](https://i.imgur.com/xMQXgEW.jpg)
目前管理頁相當簡便，只有兩個功能，修改搶團時間和清除搶團結果，修改搶團時間須按照指定格式 yyyy/mm/dd hh:MM:ss格式填寫；若填寫clear會清除搶團結果；若格式有誤會填寫其他東西會跳到錯誤頁面


## 未來發展

### 短期目標

* 在表格加入時間
* 修復未照順序填寫造成的錯誤
* 優化GUI

理想在這學期做完

### 中長期目標

* 可以從後台修改搶團結果
* 加入手機板頁面
* 可以從頁面增加減少搶團數

