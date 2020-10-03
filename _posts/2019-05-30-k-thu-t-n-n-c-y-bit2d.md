---
layout: post
published: true
title: 'Kỹ thuật nén cây BIT2D '
date: '2019-05-30'
tags:
  - CP
  - BIT2D
  - DS
---
Xin chào, dạo này mình khá chán nên toàn làm những chuyện ngu ngốc, do đó mình chạy đi viết cái blog này cho đỡ chán ._. 

Bài viết này mình nói tới một kỹ thuật khá hay của cây BIT2D (hay còn gọi là cây fenwick 2D), do đó những bạn nào chưa thành thạo BIT2D có thể bỏ qua bài này. Bài này vận dùng nhiều kiến thức của rời rạc hoá, các bạn có thể tham khảo ở [Vnoi Wiki](http://vnoi.info/wiki/algo/trick/Roi-rac-hoa-va-ung-dung)

## Kỹ thuật nén cây BIT2D là gì?
Thông thường, cây BIT2D (hay cả 1D) đều phải chứa dữ liệu trong một mảng 2D (hoặc 1D) với độ lớn ngang với kích thước các truy vấn. Do vậy, khi mà các truy vấn có giới hạn lớn thì thường các bạn sẽ dùng map (trong c++) để lưu cây BIT, điều này làm cho độ phức tạp tăng thêm log của map nữa. Kỹ thuật nén cây BIT2D là kỹ thuật để dùng cây BIT2D trong những bài toán yêu cầu bảng lớn (1e18\*1e18 vẫn làm được), **với điều kiện phải biết trước tất cả các truy vấn**. Mình học được kỹ thuật này trong 1 lần làm contest của VNOI.

## Bắt đầu thôi
Xét bài toán: Cho một bảng hình chữ nhận kích thước m\*n, ta có q truy vấn thuộc một trong 2 loại: truy vấn update một ô (u,v) lên x, và truy vấn lấy tổng hình chữ nhật (1,1) -> (u,v). giới hạn m,n,q là 1e6.

Nếu m\*n nhỏ (m\*n tầm 1e6) thì ta có thế dùng một cây BIT2D bình thường, code nó đơn giản thế này:
```c++
void update2D(int x, int y, int val)  //cập nhật điểm (x,y) lên val
{
    for (; x <= m; x += x & -x)
        for (int v = y; v <= n; v += v & -v)
            node[x][v] += val;
}
int get2D(int x, int y)  //lấy tổng hình chữ nhật (1,1) -> (x,y)
{
    int res = 0;
    for (; x > 0; x -= x & -x)
        for (int v = y; v > 0; v -= v & -v)
            res += node[x][v];
    return res;
}
//node là một cấu trúc dữ liệu mảng 2D, có thể thay bằng map
```
Với cách cài đặt trên, khi mảng m hoặc n quá lớn thì không đủ bộ nhớ để lưu mảng node, nếu thay bằng map thì lại phải mất thêm log.

Nhìn tinh tế một chút ta sẽ thấy, với mỗi truy vấn get2D hoặc update2D, số nút trên cây (hay số phần tử của mảng node) bị tác động vào chỉ là O(log(m)\*log(n)), do đó ta có thể thấy, số nút thật sự cần thiết phải lưu chỉ là O(q\*log(m)\*log(n)), nhỏ hơn rất nhiều so với lưu cả bảng m\*n.

Để làm được việc này, ta tạo ra 2 hàm update và get khác, chỉ có tác dụng để tạo trước những nút cần thiết (hay còn gọi là fakeUpdate, fakeGet):
``` c++
void fakeUpdate(int x, int y) {
    for (; x <= m; x += x & -x)
        node[x].push_back(y);
}
void fakeGet(int x, int y) {
    for (; x > 0; x -= x & -x)
        node[x].push_back(y);
}
//node là một vector 2 chiều
//dễ thấy tổng số phần tử trong node chỉ là O(q\*log(m)\*log(n)) 
```
Sau khi tạo được mọi nút cần thiết, ta tiến hành rời rạc hoá các vector node, sau đó thực hiện truy vấn như bình thường, lưu ý mảng node bây giờ chỉ dùng để ánh xạ lại index chứ không có tác dụng lưu các giá trị của cây BIT nữa, ta làm cây BIT trên một mảng khác, các bạn có thể đọc đoạn code dưới đây để hiểu thêm.
``` c++
void update2D(int x, int yy, int val) {
    for (; x <= n; x += x & -x)
        for (int y = lower_bound(node[x].begin(), node[x].end(), yy) - node[x].begin() + 1; y <= node[x].size(); y += y & -y)  //tìm vị trí sau khi rời rạc
            BIT[x][y - 1] += val;
}
int get2D(int x, int yy) {
    int res = 0;
    for (; x > 0; x -= x & -x)
        for (int y = lower_bound(node[x].begin(), node[x].end(), yy) - node[x].begin() + 1; y > 0; y -= y & -y)
            res += BIT[x][y - 1];
    return res;
}
```

Các bạn có thể tham khảo code full ở [notebook của anh RR](https://github.com/ngthanhtrung23/ACM_Notebook_new/blob/master/DataStructure/BIT2D.h)
## Bài tập áp dụng
[Bài G - Thi thử VNOI](https://codeforces.com/group/FLVn1Sc504/contest/212925/problem/G) (các bạn phải vào [group]( https://codeforces.com/group/FLVn1Sc504) trước mới có thể xem được bài này).

## Nguồn tham khảo
[Editorial của Thi thử VNOI](https://codeforces.com/group/FLVn1Sc504/blog/entry/2229)
