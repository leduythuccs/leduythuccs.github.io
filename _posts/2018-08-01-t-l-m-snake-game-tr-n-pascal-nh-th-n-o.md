---
layout: post
published: false
title: Tớ đã làm Snake Game trên Pascal như thế nào
date: '2018-08-01'
tags:
  - CP
---
Tối qua tớ không ngủ được nên ngồi code Snake Game bằng Pascal :v thấy cũng thú vị nên chia sẽ cho mọi người cách làm. Các cậu có thể chơi demo ở [đây](https://github.com/leduykhongngu/SnakeGame), mình có để full source code luôn đó :v 
### Điều cần biết:
- Các cậu nên biết sơ về thư viện Graph của Pascal là được :v Các cậu có thể xem thêm ở [đây](https://www.freepascal.org/docs-html/rtl/graph/index.html)

### Bắt đầu thôi
- Hiển nhiên là chơi Snake Game thì phải có con rắn rồi, ở đây mình viết một class TSnake, cơ bản thì nhìn nó như thế này:
```objectpascal
type    int = SmallInt;
        TPoint = record
                x,y:int;
        end;
        TMyvector = specialize TVector<TPoint>;
        TSnake = class
                private
                        Snake:TMyVector;
                        Head:TPoint;
                public
                        constructor Create();
                        procedure Update(key:int);
                        procedure Show();
                        function CheckCut(P:TPoint; pos:int=1):boolean;
        end;
```
Giải thích một chút, Snake là một Vector chứa thân của con rắn :v và Head là đầu của nó


