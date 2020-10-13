# web_crawler

## Description

這個資料夾的問題集將對應到 [yiyu0x/web_crawler](https://github.com/yiyu0x/web_crawler) Issue

## 貢獻流程

### 找尋中意的問題並在本地端設定好

1. 到 []() 專案資料夾找尋自己喜歡的 Issue
2. 到 [yiyu0x/web_crawler](https://github.com/yiyu0x/web_crawler) 右上方點一顆星星
3. 點選右上方的 Fork 按鈕，Fork 一份專案到你的帳號底下
4. 下載專案的 zip 檔
5. 解壓縮並開始解題，注意這份專案是拿來測試用，請勿 push 回自己的 branch

### 解題後使用指令將更改送回 GitHub 端

1. 解完題後，使用 `git clone <https url>` 將專案拉下來
2. 使用 `git remote -v` 查看專案來源，並使用 `git remote add pull https://github.com/yiyu0x/web_crawler.git` 將原始專案的來源加入 remote，這個小步驟讓原始專案有更新的時候，你可以隨時從原始專案獲取最新資源，省下很多不必要的 debug。
3. 使用 `git checkout -b <你喜歡的 branch 名稱>` 切換到新的 branch
4. 把寫好的程式碼複製到對應的檔案
5. 使用 `git status` 確認有新增程式碼
6. `git add <file> or -A` 將更改送到暫存區
7. `git commit -m <title> -m <description(如果有需要的話)>` 將更改送到儲存庫
8. `git remote -v` 確認要 push 回哪一個來源
9. `git push <remote name> <local branch>:<target branch>` 將變更送回 GitHub
