---
layout: post
published: true
title: Cấu trúc dữ liệu Trie
subtitle: 'Trie is love, Trie is life'
date: 2018/05/23
tags: [CP,Trie,DS]
image: /img/trie1.png
---
Xin chào, hôm nay không thấy có contest gì, cũng đang lười học nên thôi viết một cái blog về Trie – một cấu trúc dữ liệu mình cực kì thích (nếu không muốn nói là thích nhất trong tất cả các CTDL mình đã học). Ở phạm vi bài viết này, mình sẽ không nói về những thứ cơ bản của Trie (như là Trie là gì), mình sẽ nói về 1 số thứ mình thường lấy Trie để dùng, còn nếu các bạn muốn tìm hiểu thêm về trie thì có thể xem ở [vnoi](http://vnoi.info/wiki/algo/data-structures/trie).

## Vấn đề cài đặt
Trie có 2 cách cài đặt khá phổ biến, đó là cài đặt Trie bằng mảng và bằng con trỏ. Theo mình, nếu các bạn mới học, và chưa nắm rõ về con trỏ thì hãy dùng mảng, vì nếu cài Trie bằng con trỏ mà không hiểu bản chất của con trỏ (lẫn của Trie) là loạn ngay. Nhưng nếu các bạn thấy ổn, thì mình khuyên các bạn hãy cài Trie bằng con trỏ, đây là một số lý do  chủ quan của mình:
* Cài Trie bằng con trỏ (mình hay gọi là Trie động) bạn không cần phải tính toán trước bộ nhớ mảng cần khai bao (vì bạn có dùng mảng đâu?), thật ra việc tính toán này không khó, nhưng nếu bạn khai báo một mảng lớn thì có thể làm chậm chương trình của bạn (và đôi khi cũng không dùng hết độ lớn của mảng, gây phí dữ liệu). Thật ra thì nếu cài Trie bằng mảng có thể thay bằng vector, nhưng dùng vector sẽ tốn thời gian truy cập hơn, và đôi khi cũng tốn bộ nhớ hơn. 
* Cài Trie động thì bạn có thể dễ dàng cài nhiều Trie một lúc (chỉ cần tạo một gốc mới là có cây Trie mới ngay)
* Trie động có thể xóa được những nút không cần dùng tới nữa (thật ra thì ít bài toán cần phải xóa một nút ra khỏi cây Trie).
Ở trên vnoi wiki thì có code Trie động bằng Pascal, trong bài viết này mình cung cấp một phần code Trie động của mình trên C++, công dụng tương tự như code mẫu ở Vnoi wiki.

Tạo một struct TrieNode như sau:
```c++
struct TrieNode {
    TrieNode* child[26];
    int cnt;
    TrieNode() {
        for (int i=0; i<26; ++i) 
            child[i]=NULL;
        cnt=0;
    }
};
```
Hàm thêm một xâu vào Trie:  
```c++
void TrieInsert(const string &s)
{
    int n=s.length();
    TrieNode* p=root;
    for (int i=0; i<n; ++i) {
        int nxt=s[i]-'a';
        if (p->child[nxt]==NULL)
            p->child[nxt]=new TrieNode();
        p=p->child[nxt];
    }
    ++p->cnt;
}
```
Hàm kiểm tra xem xâu s có trong Trie hay không:
```c++
bool TrieFind(const string &s)
{
    int n=s.length();
    TrieNode* p=root;
    for (int i=0; i<n; ++i) {
        int nxt=s[i]-'a';
        if (p->child[nxt]==NULL)
            return false;
        p=p->child[nxt];
    }
    return p->cnt>0;
}
```
## Một số ứng dụng khác của Trie
Ứng dụng chính của Trie là quản lý một tập các xâu, với các truy vấn cơ bản như:
* Thêm một xâu vào tập hợp.
* Xóa một xâu khỏi tập hợp.
* Kiểm tra một xâu có trong tập hợp hay không.


Truy vấn 1 và 3 code trên của mình đã làm rõ, về truy vấn 2 thì dành lại cho người đọc vậy :D. 
Ngoài ra, ta hoàn toàn có thể dùng Trie để quản lý tập hợp các số (bằng cách xem một số nguyên là một xâu gồm toàn số 1 và 0), và ngoài các truy vấn cơ bản ra, một Trie quản lý tập hợp các số thì có một số truy vấn sau.


* Tìm số nhỏ thứ k trong Trie.
* Cho một số a đã có trong Trie, tìm xem nó là số lớn thứ mấy trong Trie.
Trong bài viết này, mình sẽ không cung cấp code mẫu của Trie quản lý tập số, cũng như code của 2 truy vấn trên, xem như đây là bài tập dành cho bạn đọc :D. 

## Bài tập luyện tập
Bài tập về Trie quản lý tập các xâu thì các bạn có thể xem ở vnoi wiki, ở đây mình đưa ra vài bài (có thể dùng) Trie quản lý các số để giải:
* [Codeforces 948D]( http://codeforces.com/problemset/problem/948/D)
* [Codeforces 706D](http://codeforces.com/problemset/problem/706/D)
* [Codeforces 979D]( http://codeforces.com/problemset/problem/979/D)
* [VOJ – VOXOR]( http://vn.spoj.com/problems/VOXOR/)
* [VOJ – MEDIAN]( http://vn.spoj.com/problems/MEDIAN/)
* [VOJ – ORDERSET]( http://vn.spoj.com/problems/ORDERSET/) (mình rất khuyết khích các bạn làm bài này bằng Trie, yêu cầu nhiều truy vấn trong 1 bài)
## Nguồn tham khảo
[Vnoi](http://vnoi.info/wiki/algo/data-structures/trie)
