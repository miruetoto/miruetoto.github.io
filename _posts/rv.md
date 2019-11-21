1. 저자들이 제안하는 방법이 (1) 어떤 방법과 비교하여 (2) 어떠한 점이 우수한지 (3) 왜 그러한지 명확하게 설명하고 있지 않다. 
저자들은 제안하는 방법이 기존방법들에 비하여 brightness preservation, noise tolerance, unusual looks 등에 강점을 보인다고 서술하고 있다. 
이 설명은 모호하다. 예를들어 [1] 에서는 BBHE가 기존의 (1) HE에 비해서 (2) brightness preservation 의 측면으로 볼때 우수한 성능을 보인다고 설명하고 있다. 그리고 (3) 그 이유는 Ch 3에서 설명하고 있다. [2] 에서는 XX가 XX에 비하여 XX의 측면에서 우수하다고 설명한다. 저자들의 방법은 (1) 타겟이 명확하지 않으며 (2) 어떠한 점이 우수한지 명확하게 하지 않았으며 (3) 우수한 이유를 명확히 설명하지 않는다. 

2. 저자들의 방법이 다른 방법들과 가장 구별되는 특징은 kumaraswamy distribution을 사용하였다는 점이다. 
histogram splitting과 같은 방법은 이미 BBHE등에서 사용된적 있기 때문에 저자들이 제시한 독특한 방법이라고 보기 어렵다. 
따라서 저자들은 kumaraswamy distribution을 선택한 이유와 kumaraswamy distribution을 선택하였을때의 장점을 명확하게 설명해야 한다. 
**The most distinguishing feature of the authors' methods from other methods is that they used kumaraswamy distribution.
(Histogram splitting is not an author's own creative method, because it has already been used in other papers, such as BBHE and BEASF).
Therefore, the authors should clearly explain why they chose the kumaraswamy distribution and the advantages of choosing the kumaraswamy distribution. But the authors did not make this effort.**


3. 몇몇 실험결과들을 신뢰할 수 없다. **Some experimental results are unreliable.**
- Table 1에 제시된 CCL data set 에서 proposed method 의 Entropy가 9.8981 이라고 되어있는데 이것은 오타인것 같다. **In the CCL data set presented in Table 1, the Entropy of the proposed method is 9.8981, which seems to be a typo.**
- BEASF는 HE에 비하여 brightness preservation의 측면에서 우수하다고 알고 있다. 하지만 MCL dataset에서의 결과를 보면 그렇지 않다. 뿐만 아니라 이 값이 다른방법들이 비하여 너무 큰 값(0.9051)을 가지고 있는 점이 이상하다. **BEASF is known to be superior to HE in terms of brightness preservation. However, the result in the MCL dataset is not. In addition, it is strange that this value is too high (0.9051) compared to other methods.** 
- 제안된 방법의 엔트로피가 내 예상보다 높게 나온다. 그림 3에서 살펴본 바에 의하면 제안된 방법의 히스토그램은 Uniform distribution과 거리가 멀어보인다. 오히려 평균쪽에 값이 집중된것 처럼 보여 다른방법들보다 엔트로피가 낮게 나와야 할 것으로 예상되는데 그렇지 않다. **The entropy of the proposed method is higher than my expectations. As shown in Figure 3, the histogram of the proposed method is far from the uniform distribution(values are concentrated on the average). Therefore, to my understanding, the entropy of the proposed method should be lower than the results in table 1.** 

4. 논문의 주제인 image enhencement 는 통계학에서 관심을 가지는 영역이 아니다. 
따라서 image enhencement 와 관련된 논문이 통계학 저널에 실리기 위해서는 image enhencement 을 구현하는 차별적 요소가 통계학과 밀접한 관련이 있어야한다고 나는 생각한다. 
즉 저자들이 제안한 방법에서 통계학이 가지는 contribution 이 매우 커야한다. 
하지만 저자들의 논문에서 통계와 연관이 있는 단어는 히스토그램과 kumaraswamy distribution 뿐이다. 
이중 histogram 은 제안된 방법이 기존의 다른방법과 뚜렷한 차별점을 가지는 요소는 아니다. 
그럼 남은것은 kumaraswamy distribution 뿐인데 이 분포를 단순히 사용하였다는 것이 통계저널에 실을만한 충분한 사유가 된다고 생각하기 어렵다. 
**The subject of the paper, image enhencement, is not an area of interest in statistics.
Therefore, in order for a paper related to image enhencement to be published in our journal, I believe that the distinctive elements that authors implement image enhencement should be closely related to statistics. In other words, the role of statistics in the methods proposed by the authors should be very critical. However, the only words associated with statistics in the author's paper are 'histogram' and 'kumaraswamy distribution'.
Of these, 'histogram' is not a factor that makes the proposed method distinct from other methods.
Then, the only thing left is the 'kumaraswamy distribution'. However, I don't thick that the use of this distribution does not indicate that the author's method is closely related to statistics.**
