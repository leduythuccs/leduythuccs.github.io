---
layout: post
published: true
title: 'Một số bài toán quy hoạch động cổ điển - phần 1'
date: '2019-08-14'
tags:
  - CP
  - DP
---

Xin chào, mình đang hơi chán vì chưa biết làm gì, nhân tiện thì mình viết cái blog này để chia sẻ một số bài/dạng bài quy hoạch động (QHĐ/dynamic programming/DP) mà mình cảm thấy nó "cổ điển". Định nghĩa "cổ điển" với mình là những bài mà cái dạng thuật toán của nó rất khó nghĩ ra nếu chưa biết, kiểu bất khả thi để nghĩ ra thuật toán trong giờ vậy. 

QHĐ là một kỹ thuật giải các bài toán phức tạp bằng cách chia nhỏ nó ra thành các bài toán con, giải các bài toán con sau đó bằng một cách nào đó hợp chúng lại để có thể tính toán kết quả cho bài toán mẹ. 

Ở blog này mình chỉ chia sẻ một số dạng mà mình thấy nó hay, nhưng mình sẽ không đi vào chi tiết từng dạng, mà chỉ dừng ở việc cung cấp tên, việc học nó các bạn có thể lấy keyword để tìm hiểu thêm. Mình liệt kê dựa trên trí nhớ và cảm tính của mình nên rất có thể sẽ không đầy đủ, bạn nào có góp ý bổ sung nào thì nói cho mình nhé :>



### 1. Fibonacci

Bài này thì huyền thoại rồi, gần như luôn là ví dụ để hiểu hơn DP là gì. 
Tóm tắt bài này chính là việc tính dãy số Fibonacci, dãy số này được định nghĩa như sau:

$$F_i= \begin{cases} i, \text{if} \space i\le1 \\ F_{i-1}+F_{i-2}, \text{if} \space i\ge 2 \end{cases}$$

Cài đặt công thức này không khó và điều mà rất nhiều người đã biết đó là việc tính số $$F_n$$ có thể tính được bằng cách  **nhân ma trận** với độ phức tạp là $$O\left(2^3logn\right)=O\left(logn\right)$$. 

Tổng quát hơn, nếu một dãy số bất kì mà trạng thái sau là một **tổ hợp tuyến tính** của các trạng thái trước thì (về mặt lý thuyết) ta luôn có thể dùng nhân ma trận để tính được: 

$$F_i= \begin{cases}  a_i, \text{if} \space i < m \\ \sum_{k=1}^{m}c_k*F_{i-k}, \text{if} \space i \ge m \end{cases}$$

Độ phức tạp để tính $$F_n$$ bây giờ là $$O\left(m^3*logn\right)$$
### 2. Dãy con tăng dài nhất (Longest Increasing Subsequence - LIS)
Bài này thì nổi tiếng không kém gì bài trên, bạn nào đọc sách "Giải thuật và lập trình" của thầy Lê Mình Hoàng chắc chắn bài này là bài DP đầu tiên mà các bạn đọc.

Bài toán tìm dãy con tăng dài nhất là tìm ra một dãy con của một dãy cho trước, sao cho các phần tử của dãy con đó đã được sắp xếp (mà vẫn giữ thứ tự tương đối như trong dãy ban đầu) tăng dần từ nhỏ tới lớn và dãy con đó là dài nhất có thể, dãy con tìm được không nhất thiết phải liên tục. 

Bài này cung cấp 2 kiến thức rất quan trọng: một là công thức truy hồi, hai là cách tối ưu một công thức quy hoạch động.

Tổng quát, công thức quy hoạch động của các dạng này có thể viết như sau: 

$$F_i= Oper(F_i,F_j), j<i \space \& \space  require$$

Ở đây Oper là một hàm số tuỳ theo bài toán, require là điều kiện kèm theo cũng tuỳ theo bài toán. Trong bài LIS thì $$Oper(a,b)$$ chính là $$max(a,b+1)$$ còn requeire là điều kiện $$a_j<a_i$$

Nếu một bài toán có công thức quy hoạch động dạng này thì nó có thể tính được trong độ phức tạp $$O((X+Y)*n^2)$$, với $$X,Y$$ là độ phức tạp của việc tính hàm $$Oper$$ và kiểm tra điều kiện $$require$$.

Một số công thức có thể dùng các cấu trúc dữ liệu, thuật toán để tối ưu, giảm độ phức tạp, ví dụ bài LIS có thể dùng chặt nhị phân, Fenwick Tree, Segment Tree để tối ưu xuống còn $$O(nlogn)$$

### 3. Dãy con chung dài nhất (Longest Common Subsequence - LCS)
Bài toán tìm dãy con chung dài nhất là tìm ra một dãy con dài nhất mà nó xuất hiện trong cả 2 dãy cho trước. Nghĩa là, nó có thể nhận được từ dãy đầu tiên bằng cách xoá đi một số phần tử của dãy đó, tương tự với dãy thứ hai.
Với bài toán này, bản thân mình thấy nó cung cấp một cách đặt hàm QHĐ mới, và cũng cho thấy việc đặt hàm để quy hoạch động cũng ảnh hưởng rất nhiều tới độ phức tạp tính toán. 

Có 2 cách đặt hàm phổ biến mà mình thấy: 

 1.  $$F_{i,j}$$ là dãy con chung dài nhất của 2 xâu $$A,B$$ nằm trong đoạn $$[1;i]$$ của xâu A và đoạn $$[1;j]$$ của xâu B, dãy con đó phải kết thúc ở $$i$$ và $$j$$ (nghĩa là phải chọn phần tử $$A_i,B_j$$, tương đương với việc hàm chỉ có giá trị khi $$A_i=B_j$$). ĐPT của cách này là $$O(n^{2}*m^{2})$$, có thể tối ưu xuống $$O(n*m)$$
 2. $$F_{i,j}$$ là dãy con chung dài nhất của 2 xâu $$A,B$$ nằm trong đoạn $$[1;i]$$ của xâu A và đoạn $$[1;j]$$ của xâu B, nhưng dãy con đó **không** bắt buột kết thúc ở $$i$$ và $$j$$. ĐPT của cách này là $$O(n*m)$$

Qua đó, có thể thấy việc đặt hàm như thế nào rất ảnh hưởng tới cách tính hàm cũng như độ phức tạp trong tính toán. Mình thấy đa số mọi người đều biết cách 2 (vì nó nằm ngay trong sách), nhưng lại không nhiều người biết cách 1. Theo mình, cách một dễ tổng quát hoá hơn là cách 2, chúng ta có thể thêm một số điều kiện như: 2 phần tử liền kề trong dãy con được chọn phải nguyên tố cùng nhau, phải lớn gấp đôi nhau , ... nếu có những điều kiện này thì cách 2 không giải được, nhưng cách 1 thì có. 

### Hết phần 1.
