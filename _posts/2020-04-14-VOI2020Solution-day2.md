---
published: true
title: Ngày 2 - Lời giải đề thi HSG quốc gia môn tin học năm 2020
layout: post
date: '2020-04-14'
tags:
  - CP
  - VOI
---
Solution ngày 1: [blog](/2020-02-23-VOI2020Solution-day1)

Đề thi ngày 2: [PDF](/data/VOI2020/VOI2020_day_2.pdf)

Link nộp bài: [VOI2020](https://codeforces.com/group/FLVn1Sc504/contest/266446). Các bạn cần vào group: [VNOI - Vietnam Olympiad in Informatics](https://codeforces.com/group/FLVn1Sc504) ở codeforces trước nếu không vào được link contest. 

Với các bài, nếu đề quá dài mình sẽ tóm tắt lại đại ý trước khi đi vào lời giải. Mình sẽ chủ yếu đi vào lời giải cho sub cuối cùng, nhưng sẽ nói sơ qua các cách vét điểm. Nếu các bạn có thắc mắc gì thì có thể comment vào [post này](https://www.facebook.com/leduy.khongngu/posts/2587815004810445) hoặc nhắn tin cho mình. 

- [Bài 4](#bài-4-light)
  * [Tóm tắt đề bài](#tóm-tắt-đề-bài)
  * [Lời giải](#lời-giải)
- [Bài 5](bài-5-buildnig)
  * [Tóm tắt đề bài](#tóm-tắt-đề-bài-1)
  * [Lời giải](#lời-giải-1)
- [Bài 6](#bài-6-equake)
  * [Tóm tắt đề bài](#tóm-tắt-đề-bài-2)
  * [Lời giải](#lời-giải-2)
- [Nhận xét ngày 2](#nhận-xét-ngày-2)

## Bài 4: LIGHT

- Tag: Greedy, 2D prefix sum

### Tóm tắt đề bài

Có một ma trận $$m \times n$$, mỗi ô mang giá trị từ 0 tới 2. Ta có $$k$$ nút bấm có dạng $$(r_i, c_i), (x_i, y_i)$$. Khi bấm một nút thì toàn bộ các ô nằm trong ma trận con của nút đó được tăng giá trị lên 1 (trong modulo 3, nghĩa là 2 thì sẽ chuyển về 0). Nhiệm vụ của bạn là tìm số lần bấm ít nhất để toàn bộ ma trận có giá trị là 1, hoặc toàn bộ có giá trị là 2. Một điều kiện **rất quan trọng** là $$(r_i, c_i)$$ khác nhau với mọi $i$. 

### Lời giải

Một số nhận xét trước khi làm bài:
1. Thứ tự bấm các nút không quan trọng.
2. Số lần bấm 1 nút không quá 2 lần.

#### Subtask 1: $$m = 1, n \leq 10$$

Subtask này nhiều cách để trâu lắm, dự trên nhận xét 2 ở trên, có thể sinh $$3^k$$ cách bấm rồi kiểm tra.

#### Subtask 2: $$m * n \leq 10^3$$

Hãy xem xét cách biến đổi toàn bộ bảng về một giá trị $$t$$. Ta sẽ cố gắng biến đổi ô $$(1, 1)$$ về $$t$$, sau đó là ô $$(1, 2), (1, 3), ..., (1, n)$$, sau đó tiếp tục tới hàng thứ 2, 3, ... 

Xét ô $$(1, 1)$$, rõ ràng duy nhất chỉ có nhiều nhất một nút bấm ảnh hưởng tới nó, vậy nếu ô $$(1, 1)$$ mà khác giá trị $$t$$, rõ ràng ta cần phải bấm (và ta biết chính xác là cần phải bấm bao nhiêu lần), còn nếu không có nút bấm thì rõ ràng không thể biến toàn bộ bảng về giá trị $$t$$. Điều này thực hiện được là nhờ điều kiện tất cả $$(r_i, c_i)$$ của mọi truy vấn là phân biệt (nếu không có điều kiện đó thì mình cũng không biết bài này làm thế nào). 

Sau khi bấm xong ở ô $$(1, 1)$$ thì ta xem như là xóa nó đi, tương tự sang ô $$(1, 2)$$ cũng chỉ có nhiều nhất 1 nút bấm ảnh hưởng tới nó. Tiếp tục quy nạp thì ta sẽ xét được hết bảng.

Do giới hạn nhỏ, nên mỗi lần bấm nút ta có thể thực hiện duyệt qua toàn bộ ô được ảnh hưởng bởi nút bấm đó và điều chỉnh lại giá trị.

#### Subtask 3: $$m * n \leq 10^5$$

Ở subtask này thì việc duyệt qua toàn bộ ô bị ảnh hưởng là không khả thi, và hiển nhiên là ta cần phải optimize chỗ này, ta xem xét kĩ hơn ở những việc cần làm:

1. Cập nhật toàn bộ ô trong một hình chữ nhật lên một giá trị $$t$$
2. Tính giá trị tại một ô. 

Tới đây thì nhiều bạn dùng cây [Fenwick tree 2D](https://www.geeksforgeeks.org/two-dimensional-binary-indexed-tree-or-fenwick-tree/) để thực hiện các truy vấn này, độ phức tạp là $$O(m \times n \times log(m) \times log(n))$$. 

Nhưng nếu để ý hơn thì ta nhận thấy là ở các truy vấn lấy giá trị tại một ô, các ô được lấy "tăng dần" (ta lấy ô $$(1, 1)$$ rồi tới ô $$(1, 2), (1, 3), \dots$$, do đó ta chỉ cần một mảng prefix sum 2D là đủ, và dùng thêm trick [này](https://codeforces.com/blog/entry/50185?#comment-340926). 

Độ phức tạp là $$O(m \times n)$$

Code tham khảo: [LIGHT.cpp](/data/VOI2020/LIGHT.cpp)

## Bài 5: BUILDING

- Tag: Graph, sweep line

### Tóm tắt đề bài:

Có một số hình chữ nhật trong mặt phẳng tọa độ $$Oxy$$, các hình chữ nhật có thể chạm vào nhau nhưng không đè lên nhau. Ta tạo một đồ thị vô hướng, với các đỉnh là các hình chữ nhật, 2 đỉnh có cạnh nối khi và chỉ khi 2 hình chữ nhật tương ứng chạm nhau. Trong đồ thị mới có thể có một số cầu, khi xóa cây cầu đó đi thì một thành phần liên thông sẽ bị tách ra làm 2, gọi số lượng đỉnh 2 bên lần lượt là $$A$$ và $$B$$, ta cần tìm giá trị $$\|A-B\|$$ nhỏ nhất. 

### Lời giải:

Bài này phần khó nhất là việc dựng đồ thị lên, còn việc tìm $$\|A-B\|$$ nhỏ nhất là bài khá cơ bản rồi. Các bạn có thể làm bài [REFORM](https://codeforces.com/group/FLVn1Sc504/contest/274830/problem/O) ở group [VNOI - Vietnam Olympiad in Informatics](https://codeforces.com/group/FLVn1Sc504) để rõ hơn cái kỹ thuật này. Nên ở mỗi subtask mình sẽ chú ý vào việc dự đồ thị hơn.

Các nhận xét trước khi làm bài:
1. Đồ thị trong bài là đồ thị phẳng, nên số lượng cạnh không quá $$3\times n$$, đọc thêm về đồ thị phẳng ở [đây](https://en.wikipedia.org/wiki/Planar_graph)
2. Một điểm thì có nhiều nhất 4 hình chữ nhật chứa có.

#### Subtask 1: $$n \leq 10^3$$

Ở subtask này ta có thể duyệt qua mọi cặp hình chữ nhật rồi xem nó có kề nhau hay không.

#### Subtask 2: $$n \leq 10^5$$, các tọa độ không vượt quá $$10^3$$

Ở subtask này, do tọa độ không hề lớn, nên với mỗi tọa độ ta có thể biết được những hình chữ nhật nào chứa điểm này, từ đó dựng cạnh. Ta có thể áp dụng kỹ thuật tổng 2D giống bài 4, nhưng ở đây thay vì tổng thì là một set các điểm. 

#### Subtask 3: $$n \leq 10^5$$, các tọa độ không vượt quá $$10^9$$

Ta xét một bài toán đơn giản hơn: có $$n$$ đoạn thẳng trên trục $$Ox$$, hãy in ra các cặp đoạn thẳng có điểm chung. 

Bài toán trên thì có thể giải đơn giản bằng sweep line và set (đừng sợ chữ "sweep line", nó thật ra chỉ là duyệt qua các tọa độ tăng dần thôi :v): 
1. Tách các đoạn thẳng làm 2 đầu, tạm gọi là đầu mở và đóng.
2. Duyệt các tọa độ tăng dần, nếu ta gặp đầu mở, ta ném nó vào set. Nếu ta gặp đầu đóng, rõ ràng đầu này sẽ có điểm chung với toàn bộ các đầu mở đang nằm trong set, vậy nên ta in các cặp đó ra, và xóa đầu đóng tương ứng.

Quay về bài toán gốc, thì thật sự nó cũng giống như bài toán mình vừa nói, mỗi hình chữ nhật bạn có thể xem nó như là 4 đoạn thẳng, tổng cộng có $$n \times 4$$ đoạn thẳng. Ta xét các đoạn thẳng có cùng tọa độ $$x$$ (hoặc $$y$$) rồi tìm những cặp đoạn thẳng có điểm chung. Ta không sợ số cặp có điểm chung lớn, vì số cạnh thật sự của đồ thị không vượt quá $$3 \times n$$

Độ phức tạp của việc dựng đồ thị là $$O(nlogn)$$ (mất log cho phần sort các tọa độ tăng dần), độ phức tạp của phần tìm $$\|A-B\|$$ là $$O(n)$$.

Code tham khảo: [BUILDING.cpp](/data/VOI2020/BUILDING.cpp)

## Bài 6: EQUAKE

- Tag: DP on tree

### Tóm tắt đề bài:

Có một cây gồm $$n$$ nút, có trọng số, trên mỗi nút $$u$$ có $$p_u$$ nhân viên, và có một xe có thể chở $$c$$ nhân viên trong 1 chuyến, $$c$$ là số cố định cho toàn bộ nút. Để chuyển $$x$$ nhân viên từ nút $$i$$ tới nút $$j$$ (kề nhau) thì tốn chi phí là $$\lceil \frac{x}{c} \rceil \times d(i, j)$$, với $$d(i, j)$$ là trọng số cạnh nối giữa $$i, j$$. Tính tổng chi phí bé nhất để di chuyển nhân viên sao cho lượng nhân viên chênh lệch giữa toàn bộ các nút là nhỏ nhất. 

### Lời giải:

Tạm gọi $$S$$ là tổng số nhân viên trên toàn bộ nút, $$m = S \% n$$
Nhận xét:
1. Nếu $$m=0$$ thì ở kết quả, toàn bộ nút có lượng nhân viên bằng nhau.
2. Ngược lại thì có $$m$$ nút có số lượng nhân viên là $$HI = \lfloor \frac{S}{n} \rfloor + 1$$, các nút còn lại có số lượng nhân viên là $$LOW = \lfloor \frac{S}{n} \rfloor$$

#### Subtask 1: $$n = 3$$

Với $$n=3$$ thì chỉ là xét linh tinh xem mỗi nút có bao nhiêu nhân viên thôi :v 

#### Subtask 2: $$n \leq 3000$$, cây có dạng đường thẳng

Cho đơn giản thì ta xem cây nối với nhau theo $$1-2-3-4-...-n$$

Xét trường hợp $$m=0$$ (mọi nút có cùng lượng nhân viên ở kết quả cuối cùng). Xem như ta đứng ở nút 1, và ta bị thiếu nhân viên, rõ ràng ta cần phải lấy nhân viên ở nút 2. Ngược lại nếu ta dư nhân viên thì ta cần đẩy lượng nhân viên đó sang nút 2. Tương tự khi ta xét tới nút 2, lúc này nút 1 chắc chắn đã đủ nhân viên rồi, ta xét tương tự thì cũng sẽ biết được nút 2 cần lấy hay đưa nhân viên tới nút 3, ... 

Nhưng nếu $$m \neq 0$$, thì ta còn phải xác định được nút nào cần có nhiều nhân viên hơn nút còn lại. Tới đây thì ta dùng quy hoạch động: 

- Gọi $$F(u, i)$$ là tổng chi phí bé nhất để di chuyển nhân viên sao cho trong các nút từ 1 tới $$u$$ đã có $$i$$ nút có $$HI$$ nhân viên. Lúc này kết quả là $$F(n, m)$$.
- Việc chuyển trạng thái thì cũng khá đơn giản, ở nút $$u$$ ta chỉ có 2 option là:
1. Hoặc nút $$u + 1$$ có $$HI$$ nhân viên: chuyển qua trạng thái $$F(u + 1, i + 1)$$
2. Hoặc nút $$u + 1$$ có $$LOW$$ nhân viên: chuyển qua trạng thái $$F(u + 1, i)$$. 

Việc tính chi phí chuyển thì do ta biết đượng số lượng nhân viên cần thiết của trạng thái $$F(u, i)$$ (chính bằng $$u * LOW + i$$), nên ta biết được là ở đó đang dư hay thiếu nhân viên, từ đó biết là tối chi phí di chuyển như thế nào. 

Độ phức tạp là $$O(n \times m) = O(n^2)$$

#### Subtask 3: $$n \leq 3000$$

Subtask này thì từ subtask 2 ta có thể chuyển nó thành DP trên cây (mọi người hay gọi là Knapsack on tree).  $$F(u, i)$$ là tổng chi phí bé nhất để di chuyển nhân viên sao cho trong các nút ở cây con gốc $$u$$ thì có $$i$$ nút có $$HI$$ nhân viên. Tạm xem gốc của cây là 1 thì kết quả là $$F(1, m)$$.

Việc tính $$F$$ thì nó đơn thuần là knapsack rồi, nhưng khó ở chỗ là nếu làm không khéo thì chỗ DP nó sẽ là $$O(n^3)$$, các bạn có thểm tham khảo link [này](https://codeforces.com/blog/entry/52742?#comment-367974) để tham khảo cách làm $$O(n^2)$$. 

Bài này còn một cái yêu cầu là truy vết nữa, thật sự lúc code bài này mình code chưa tới 30p là xong phần tính kết quả rồi, còn phần truy vết mình làm mãi luôn tại mình ngu :v. Các bạn nên làm bài [PTREE](https://codeforces.com/group/FLVn1Sc504/contest/274518/problem/E) trước để xem cách truy vết knapsack trên cây nhé. 

Code tham khảo: [EQUAKE.cpp](/data/VOI2020/EQUAKE.cpp)

## Nhận xét ngày 2:

So với ngày 1 thì mình thấy ngày 2 có phần dễ nghĩ ra thuật hơn, ví như bài 5 mình thấy khi đọc vào rõ ràng là biết ta cần phải dựng đồ thị lên rồi làm cầu các thứ. Còn bài 6 đọc vào là biết phải làm knapsack trên cây rồi. Nhưng đề ngày 2 khó ở chỗ là khá nặng phần cài đặt cũng như cần nhiều kiến thức "lạ" (lạ ở đây là ít gặp ở VOI), như DP trên cây, sweep line (bài 5). Chung quy mình thấy ngày 1 khó hơn ngày 2. 

Có một sự thật là lúc làm VNOI Online 2020, tụi mình đã định cho một bài DP knapsack trên cây, cũng dùng cái kỹ thuật giảm xuống $$O(n^2)$$ luôn, nói chung cài đặt y chang bài 6, nhưng bọn mình để nó ở bài 4. Rồi sau đó vì 1 số lý do mà không dùng bài đó nữa. Tiếc thật sự :v. 
