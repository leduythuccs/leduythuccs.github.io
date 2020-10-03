---
published: true
title: Truy vấn cập nhật bậc thang - Polynomial Queries
layout: post
date: '2020-07-07'
tags:
  - CP
  - DS
  - Segment Tree
---
Xin chào, hôm nay mình hơi chán nên ngồi viết blog, lần này là một bài toán thao tác khá là nổi tiếng trên cấu trúc dữ liệu segment tree, Fenwick tree nhưng vẫn chưa có nhiều nguồn nói về nó bằng tiếng Việt. Cái tên gọi "cập nhật bậc thang"/"update bậc thang" là mình thường nghe những người xung quanh nói thôi chứ cũng không có tên gọi nào chính thức cho nó.

Tuy đây là một thao tác khá nổi tiếng, nhưng để học nó cần trước một số kiến thức cơ bản sau đây: 
- Segment tree (kết hợp lazy), Fenwick tree. 

Các bạn có thể học Segment tree ở [đây](https://vnoi.info/wiki/algo/data-structures/segment-tree-extend.md) và Fenwick tree ở [đây](https://vnoi.info/wiki/algo/data-structures/fenwick.md) trước khi đọc thêm bài này. 

## Bài toán 1
Cho một mảng các số nguyên $$a$$ có $$n$$ phần tử (ban đầu các phần tử khởi tạo bằng 0). Có $$q$$ truy vấn có dạng: 
- $$u$$ $$v$$: tăng $$a[u]$$ lên 1, tăng $$a[u + 1]$$ lên 2, tăng $$a[u + 2]$$ lên 3, ..., tăng $$a[v]$$ lên $$(v - u + 1)$$
Sau khi thực hiện $$q$$ truy vấn, ta cần in ra mảng $$a$$. 

### Cách giải
Nếu như truy vấn chỉ đơn giản là tăng các phần tử trong đoạn lên một hằng số thì ta có thể dễ dàng thực hiện bằng cách:

- Với mỗi truy vấn $$(u, v)$$, ta thực hiện $$a[u]$$ += $$x; a[v + 1]$$ -= $$x$$. 
- Sau khi thực hiện xong các truy vấn, ta gán $$a[i]$$ += $$a[i - 1]$$ là xong.

Ở trên là một trick mà ai cũng biết, nếu không biết thì cũng có thể làm bằng segment tree hoặc Fenwick tree.

Nhưng với bài toán này, các phần tử được tăng lên theo cấp số cộng (công sai là 1), chứ không phải là hằng số. 

Xét truy vấn $$(u, v)$$, việc cập nhật được thực hiện như sau:
- $$a[u]$$ += $$1$$
- $$a[u + 1]$$ += $$2$$
- $$a[u + 2]$$ += $$3$$
- ...
- $$a[v]$$ += $$(v - u + 1)$$

Cộng $$0 = (u - 1) - (u - 1)$$ vào vế phải của tất cả các phép biến đổi trên. 

- $$a[u]$$ += $$(1 + (u - 1)) - (u - 1) \Leftrightarrow a[u]$$ += $$u - (u - 1)$$ 
- $$a[u + 1]$$ += $$(2 + (u - 1)) - (u - 1) \Leftrightarrow a[u + 1]$$ += $$(u + 1) - (u - 1)$$
- $$a[u + 2]$$ + = $$(3 + (u - 1)) - (u - 1) \Leftrightarrow a[u + 2]$$ += $$(u + 2) - (u - 1)$$
- ...
- $$a[v]$$ += $$((v - u + 1) + (u - 1)) - (u - 1) \Leftrightarrow a[v]$$ += $$v - (u - 1)$$

Tới đây ta có thể nhận thấy điều sau: Mỗi truy vấn $$(u, v)$$ tương ứng với 2 loại truy vấn khác:
1. Giảm (trừ) tất cả các phần tử trong đoạn $$[u, v]$$ đi một lượng $$(u - 1)$$.
2. Với mỗi phần tử $$i$$ trong đoạn $$[u, v]$$, tăng $$a[i]$$ lên $$i$$. 

Rõ ràng thứ tự thực hiện của các truy vấn mới là không quan trọng, bạn có thể thực hiện hàng loạt các truy vấn 1 trước, rồi sau đó mới thực hiện truy vấn 2 (hoặc ngược lại). 
Bây giờ ta thấy truy vấn 1 chính là truy vấn cơ bản mà mình đã nói ở phần trên (tăng cả đoạn lên một hằng số). Vậy vấn đề còn lại là giải quyết truy vấn 2.

Việc xử lý truy vấn 2 có thể làm giống code sau:

Để rõ hơn thì các bạn có thể xem pseudo code sau đây. 
```
Với mọi truy vấn 2 [u, v]:
    Với mọi i nằm trong đoạn [u, v]
	a[i] += i
In ra mảng a
```
Với truy vấn 2, phần tử $$i$$ luôn được tăng lên một lượng cố định là $$i$$. Vậy thì thay vì ta thực hiện tăng lên một lượng cố định mỗi truy vấn, ta chỉ cần ĐẾM số lần phần tử $$i$$ được tăng, sau đó lấy $$i * cnt[i]$$ chính là lượng mà phần tử $$i$$ cần tăng:
```
Với mọi truy vấn 2 [u, v]:
    Với mọi i nằm trong đoạn [u, v]:
	cnt[i] += 1
Với i trong đoạn [1, n]:
    a[i] += i * cnt[i];
In ra mảng a
```
Hai code mình vừa trình bày đều có độ phức tạp như nhau, nhưng ở code 2, thì việc tăng cả tất cả các phần tử của mảng $$cnt$$ lên 1 thì nó cũng giống với truy vấn cơ bản ban đầu (tăng cả đoạn lên một hằng số), nên ta có thể tăng tốc nó lên được. Cuối cùng thì ta có một cái code na ná thế này <(")
```c++
for (moi truy van [u, v]) {
    //Tách ra làm 2 truy vấn.
    //Truy vấn 1: giảm đoạn [u, v] đi (u - 1)
    b[u] -= u - 1;
    b[v + 1] += u - 1;
    //Truy vấn 2: a[i] += i -> cnt[i] += 1
    cnt[u] += 1;
    cnt[v + 1] -= 1;
}
for (int i = 1; i <= n; ++i) {
    b[i] += b[i - 1];
    cnt[i] += cnt[i - 1];
    a[i] = b[i] + i * cnt[i];
}
```
Tới đây thì ta xong bài toán cơ bản đầu tiên. Độ phức tạp $$O(n)$$

## Bài toán 2
Cho một mảng các số nguyên $$a$$ có $$n$$ phần tử (ban đầu các phần tử khởi tạo bằng 0). Có $$q$$ truy vấn thuộc 1 trong 2 dạng: 
- $$1$$ $$u$$ $$v$$: tăng $$a[u]$$ lên 1, tăng $$a[u + 1]$$ lên 2, tăng $$a[u + 2]$$ lên 3, ..., tăng $$a[v]$$ lên $$(v - u + 1)$$
- $$2$$ $$i$$: in ra giá trị $$a[i]$$

Bài toán này thì cũng giống với bài toán ban đầu, chỉ khác là có thêm truy vấn yêu cầu in ra giá trị $$a[i]$$. Rõ ràng để biết được giá trị $$a[i]$$ thì ta cần biết được 2 giá trị là $$b[i]$$ và $$cnt[i]$$, thì bài toán có thể phát biểu lại như sau:
Có 3 loại truy vấn:
- Giảm giá trị các phần tử trong đoạn $$[u, v]$$ của mảng $$b$$ đi $$(u-1)$$
- Tăng giá trị các phần tử trong đoạn $$[u, v]$$ của mảng $$cnt$$ lên 1
- Tính giá trị $$b[i] + i * cnt[i]$$. 

Các truy vấn này các bạn có thể giải quyết bằng 2 cây Fenwick, một cây để quản lý $$b$$, một cây để quản lý $$cnt$$, vậy là xong (hoặc làm bằng cây segment cũng được). Độ phức tạp $$O(nlogn)$$.

## Bài toán 3
Cho một mảng các số nguyên $$a$$ có $$n$$ phần tử (ban đầu các phần tử khởi tạo bằng 0). Có $$q$$ truy vấn thuộc 1 trong 2 dạng: 
- $$1$$ $$u$$ $$v$$: tăng $$a[u]$$ lên 1, tăng $$a[u + 1]$$ lên 2, tăng $$a[u + 2]$$ lên 3, ..., tăng $$a[v]$$ lên $$(v - u + 1)$$
- $$2$$ $$u$$ $$v$$: in ra tổng $$\sum_{i=u}^{v} a[i]$$

Mình lười rồi nên dành cho bạn đọc vậy <("). Hint là các bạn có thể dùng lazy để tính $$i*cnt[i]$$. 

Các bạn có thể nộp bài ở đây: [Polynomial Queries - CSES 1736](https://cses.fi/problemset/task/1736)
