### 109-2 多媒體技術與應用課堂小組專案

---

資料集來源：http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark&fbclid=IwAR1u06li3-5cW0-g5duUsCD4Eo3JxkhseahQRAFNMXOMAqQRrd1Dy0v52wo  
下載項目：  
Download left color images of object data set (12 GB) (資料集圖片)  
Download training labels of object data set (5 MB) (label 與物件類別資料)  
Download object development kit (1 MB) (label 各數值的意義)

---

ipynb 檔使用 Google Colab 執行。  
因資料集圖片過多(12GB)，因此只放入部分照片作為展示檔案及檔名格式。

`./label`：內含資料集內 label 檔案，從資料集下載 label 資料後先將資料夾改名為`label_2_origin`，接著執行`trans.py`後就可以取得符合 YOLOv4 格式的 label 檔案了。  
`./obj`：內含訓練、測試集以及`obj.names`(辨識物件類別)`obj.data`(辨識相關參數)，資料夾內的`Makefile`及 `yolov4.custom`為 ipynb 檔內所 clone 專案後需要修改的檔案部分，clone 後直接複製進原檔案位置就可以執行 make 及後續操作了。
