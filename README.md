# DeepLearning
딥러닝실습에서 작성한 코드 모음

### 모든 코드는 Colab 환경에서 작성되었습니다.


Ubuntu 18.04.5 LTS  
CPU Intel(R) Xeon(R) CPU @ 2.00GHz  
구글 colab에서 제공하는 TPU 사용  
GPU일 경우 NVIDIA-SMI 465.27  


CUDA Version: 11.2  
Python: 3.7.10  
Torch Version: 1.8.1+cu101  

<br/>
<br/>
  


# 최종 프로젝트
YOLO 기반의 Object Detectiing

### 코드 돌리는 방법(+Command used to train model)

Colab 환경이라면 런타임 메뉴 > 모두 실행으로 바로 수행 가능  


```
!mkdir convert2Yolo
%cd convert2Yolo
!git init
!git remote add origin https://github.com/ssaru/convert2Yolo.git
!git pull origin master
!pip3 install -r requirements.txt
```
이 부분에서 에러 로그가 찍혀도 코드가 작동하는 데에는 문제되지 않기 때문에 신경쓸 필요 없음  





### Explanation of hyperparameters
|argument        |type|Explanation                                               |default|
|:---------------|:----|:--------------------------------------------------------|:------|
|dataset         |voc  |Pascal VOC 2012                                          |voc    |
|image_path      |str  |/content/data/VOCdevkit/VOC2012/JPEGImages/              |       |
|label_path      |str  |/content/data/VOCdevkit/VOC2012/Annotations/             |       |
|root            |str  |/content/data/VOCdevkit/VOC2012/                         |       |
|class_path      |str  |/content/data/VOCdevkit/VOC2012/voc.names                |       |
|batch_size      |int  |batch size                                               |20     |
|epochs          |int  |epochs                                                   |20     |
|learning_rate   |float|learning rate                                            |0.01   |
|dropout         |float|dropout                                                  |0.5    |
|num_class       |int  |classes 개수                                             |20     |
|gamma           |float|scheduler gamma                                          |0.95   |
|lambda_coord    |int  |x, y, h, w에 대한 loss과 다른 loss들의 균형을 맞춰줌      |5      |
|lambda_noobj    |float|object가 있는 Grid cell과 없는 Grid cell의 균형을 맞춰줌  |0.5    |





### 결과


epoch: [1/20), Ir: 0.01, train loss: 20,1789, val loss: 1157.5538  
epoch: [2/20], Ir: 0.01, train loss: 18.7877, val loss: 100.2710  
epoch: [3/20], Ir: 0.01, train loss: 12.6009, val loss: 10.3725  
epoch: [4/20], Ir: 0.01, train loss: 9.3500, val loss: 10.2538  
epoch: [5/20], Ir: 0.01, train loss: 6.2526, val loss: 30.1056  
epoch: [6/20], Ir: 0.01, train loss: 4.9897, val loss: 3.3702  
epoch: [7/20], Ir: 0.01, train loss: 4.8530, val loss: 192.6311  
epoch: [8/20], Ir: 0.01, train loss: 9.6027, val loss: 6.2644  
epoch: [9/20], Ir: 0.01, train loss: 5.7168, val loss: 5.1407  
epoch: [10/20], Ir: 0.01, train loss: 4.7761, val loss: 8.0795  
epoch: [11/20], Ir: 0.01, train loss: 6.2644, val loss: 5.4568  
epoch: [12/20], Ir: 0.01, train loss: 61.1468, val loss: 81.9163  
epoch: [13/20], Ir: 0.01, train loss: 12.7005, val loss: 28.2273  
epoch: [14/20], Ir: 0.01, train loss: 7.5471, val loss: 18.5594  
epoch: [15/20], Ir: 0.01, train loss: 8.5272, val loss: 8.4357  
epoch: [16/20], Ir: 0.01, train loss: 15.1778, val loss: 18.5066  
epoch: [17/20], Ir: 0.01, train loss: 8.7969, val_loss: 9.9220  
epoch: [18/20], Ir: 0.01, train loss: 6.1472, val loss: 7.6366  
epoch: [19/20], Ir: 0.01, train loss: 9.0222, val loss: 5.9237  
epoch: [20/20], Ir: 0.01, train loss: 5.1753, val loss: 6.6699  




### REFERENCES



1. You Only Look Once: Unified, Real-Time Object Detection/ Joseph Redmon/ University of Washington  
2. 모두의 연구소 - 모두를 위한 Object Detection(Object Detection for All) (https://deepbaksuvision.github.io/Modu_ObjectDetection/)
