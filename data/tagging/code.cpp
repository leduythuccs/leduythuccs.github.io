/*input
Bach 182
Nghia 161
Trung 151
*/
#include <bits/stdc++.h>
using namespace std;

mt19937 rd(chrono::steady_clock::now().time_since_epoch().count());

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    // freopen("rank_text.txt", "r", stdin);
    vector<string> a;
    string s; int t;
    while (cin >> s >> t) {
        for (int i = 1; i <= t; i++) a.push_back(s);
    }
    cout << a[rd() % a.size()] << endl;
}