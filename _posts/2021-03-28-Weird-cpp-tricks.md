---
layout: post
published: true
title: 'Weid cpp tricks'
date: '2021-03-28'
tags:
  - CP
---
Blog này nhằm cung cấp một số tricks (thề mình không biết phải dịch chữ này ra như thế nào cho hợp lý) mà mình hay dùng khi code bằng C++ trong lập trình thi đấu. Lưu ý là các trick này đa số chỉ phù hợp trong lập trình thi đấu, nó giúp bạn tăng tốc độ code và vì thế có thể giảm tính đọc hiểu của code. Vì vậy hãy xem đây là tham khảo thôi nhé :3

# Mục lục:
  * [In mảng 2 chiều](#in-m-ng-2-chi-u)
  * [Lấy min/max của nhiều số](#l-y-min-max-c-a-nhi-u-s-)
  * [Structured binding](#structured-binding)
  * [Cout & return](#cout---return)
  * [Thoát nhiều vòng lặp lồng nhau](#tho-t-nhi-u-v-ng-l-p-l-ng-nhau)

## In mảng 2 chiều

Giả sử bạn có mảng 2 chiều $$a$$ với kích thước $$n \times m$$, và bạn cần in nó ra theo format: $$n$$ dòng, mỗi dòng gồm $$m$$ số cách nhau 1 dấu cách.

Code bình thường thì nó có thể như thế này:

```c++
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j)
      cout << a[i][j] << ' ';
    cout << '\n';
  }
```

Nhưng bạn có thể code thế này, cho kết quả tương tự (thật ra là không, vì ở mỗi cuối dòng không còn space nữa):

```c++
  for (int i = 1; i <= n; ++i) 
    for (int j = 1; j <= m; ++j)
      cout << a[i][j] << " \n"[j == m];
```

Thoạt nhìn thì có thể hơi lấn cấn ở đoạn `" \n"[j == m]`, lần đầu mình thấy trick này mình cũng hơi khó hiểu đoạn đó. Cơ mà thật sự thì nó rất dễ hiểu, `" \n"` là một xâu gồm 2 phần tử, phần tử 0 là space, phần tử 1 là dấu xuống dòng. Đoạn `[j==m]` chính là để truy xấu phần tử của xâu đó, nếu $$j$$ có giá trị bằng với $$m$$ thì `j==m` cho kết quả là 1 (true), vậy nó sẽ truy xuất vào phần tử 1 của xâu ở trên, chính là xuống dòng. Còn ngược lại thì nó in ra space (truy xuất vào phần tử 0).

## Lấy min/max của nhiều số

Thay vì `min(a, min(b, c))` thì các bạn có thể dùng `min({a, b, c})`, cách này có thể dùng cho nhiều hơn 3 biến luôn.


## Structured binding

Giả sử bạn có 1 vector $$a$$ gồm các `pair<int, int>`, bạn muốn duyệt hết các phần tử trong vector này thì có 2 cách phổ biến:

1. For bằng index:
```c++
  for (int i = 0; i < a.size(); ++i) {
    cout << a[i].first << ' ' << a[i].second << '\n';
  }
```
2. Range-based for loop, cách này chỉ dùng được từ c++11 trở lên:
```c++
  for (auto p : a) {
    cout << p.first << ' ' << p.second << '\n';
  }
```

Với cả 2 cách trên thì khi muốn truy xuất các giá trị first hay second thì ta phải dùng `p.first` hoặc `p.second`, nhiều khi điều này khá là phiền phức, từ c++17 trở đi ta có thể làm như sau:
```c++
  for (auto [x, y] : a) {
    cout << x << ' ' << y << '\n';
  }
```
Không chỉ có thể dùng với pair của STL, nó có thể dùng với struct của người dùng định nghĩa, tuple, ... Đây cũng là trick mình thường xuyên sử dụng nhất, vì nó làm tăng tốc độ code lên rất nhiều. 

Kỹ thuật dùng ở code trên là [Structured binding](https://en.cppreference.com/w/cpp/language/structured_binding), xuất hiện ở c++17. Các bạn còn thi HSG QG thì lưu ý điều này, bởi vì cái trick này không dùng được trong phòng thi Quốc Gia. 

## Cout & return 

Nhiều khi các bạn sẽ rơi vào trường hợp code như thế này:

```c++
int main() {
  // stuff
  if (condition) {
    cout << something;
    return 0;
  }
  // stuff
}
```

Với code trên, các bạn cần kiểm tra 1 điều kiện nào đó, sau đó sẽ in ra và kết thúc chương trình. Ta có thể rút ngắn code bằng cách vừa return vừa cout trong 1 dòng code:
```c++
int main() {
  // stuff
  if (condition)
    return !(cout << something);
  // stuff
}
```
Operator `<<` trong cout sẽ trả về một cái `ostream`, khi ta thêm `!` đằng trước nó thì sẽ giá trị `ostream` này sẽ được convert sang bool, và có giá trị là 0. Vì thế dòng lệnh trên sẽ in ra kết quả rồi sau đó `return 0`.

Có một cách khác để thực hiện trick này, cách này thì có thể return nhiều loại giá trị hơn, thay vì chỉ return 0:

```c++
int main() {
  // stuff
  if (condition)
    return cout << something, 0;
  // stuff
}
```

Ở code này, đáng lưu ý nhất là dòng `cout << something, 0;`, cái này thì liên quan tới câu lệnh có dấu `,`. Với các khối lệnh có dấu `,` thì các lệnh được ngăn cácg bởi dấu `,` sẽ được thực hiện từ trái sang phải, và giá trị trả về của khối lệnh chính là **giá trị của lệnh cuối cùng**. Vì thế, với khối lệnh `cout << something, 0` thì lệnh `cout << something` sẽ được thực hiện trước, sau đó sẽ tới "lệnh" 0, và 0 chính là giá trị trả về của khối lệnh này, do đó return sẽ nhận giá trị 0.

Trick trên cũng có thể dùng ở hàm return void, bằng cách ta ép kiểu ostream sang void:
```c++
void foo() {
  // stuff
  if (condition)
    return void(cout << something);
  // stuff
}
```

## Thoát nhiều vòng lặp lồng nhau

Giả sử ta có một cái ma trận 2 chiều $$a$$ với kích thước $$n \times m$$, ta cần tìm vị trí đầu tiên xuất hiện của phần tử $$x$$ trong ma trận đó, nếu các bạn đang lười viết hàm, và muốn viết ở main luôn để tăng tốc độ, thì có thể các bạn sẽ code một cái như thế này:
```c++
int main() {
  // stuff
  pair<int, int> pos = {-1, -1};
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j)
      if (a[i][j] == x) {
        pos = {i, j};
        break;
      }
    if (pos != {-1, -1})
      break;
  }
  // stuff
```

Cách code trên bị dài chỉ vì ta phải kiểm tra các điều kiện để thoát khỏi vòng lặp. Với nhiều vòng lặp hơn nữa thì việc thoát khỏi nó đúng là thảm hoạ. Có một số cách fix code này rất izi đó là:
1. Viết hàm. Nếu ta viết một hàm riêng thì chỉ cần return nếu tìm thấy $$x$$, không cần quan tâm tới chuyện thoát vòng lặp nữa. Nhưng cách này có thể làm giảm tốc độ code cũng như tăng số lượng hàm con lên quá mức cần thiết, một điều mà có thể là dân CP như mình không thích (không biết mọi người khác thì sao?). 
2. Dùng goto. Quên nó đi = )). 

Ở đây mình muốn giới thiệu cách dùng lambda, cách này cũng giống như là viết hàm vậy, nhưng theo mình thấy là nó code nhanh hơn cũng như là không phải thoát ra khỏi scope code hiện tại để viết hàm, mà có thể viết trực tiếp luôn:

```c++
int main() {
  // stuff
  auto pos = [&]() -> pair<int, int> {
    for (int i = 1; i <= n; ++i) {
      for (int j = 1; j <= m; ++j)
        if (a[i][j] == x) {
          return {i, j};
        }
    }
    return {-1, -1};
  }();
  // stuff
```

Code trên có thể nhìn hơi rối nếu bạn chưa quen cách dùng lambda trong c++, nhưng mà nó hoạt động thế này: `[&]() -> pair<int, int>` đoạn này là khai báo một cái lambda, nhận vào mọi biến dưới dạng pass by reference, lambda này return một cái `pair<int, int>`, đây là cách khai báo `Trailing return type`.  Có một điều đáng lưu ý là sau khi khai báo xong thì mình gọi luôn hàm lambda này (ở dòng áp chót có đoạn gọi `()`), cái này là vì ta chỉ sử dụng đoạn code này một lần duy nhất, thay vì đặt tên cho nó và tí nữa gọi, thì ta có thể gọi ngay sau khi khai báo, để nó chạy hàm này và return thứ mình cần luôn. 

Cái trick này khá hữu dụng nếu bạn cần thoát khỏi rất nhiều vòng lặp lồng nhau.


# Tổng kết

Tạm thời mình chỉ nhớ được bao nhiêu đây, khi nào nhớ tiếp mình sẽ update :v.

Các trick này có thể khiến code bạn ngắn hơn nhưng cũng có thể làm code bạn khó debug hơn, nên xem xét cái nào phù hợp thì dùng thôi nhé. 