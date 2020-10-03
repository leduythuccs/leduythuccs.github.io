#include <bits/stdc++.h>

using namespace std;
const int maxn = 305;
int n, k;
int a[maxn];
long long f[maxn][maxn][maxn >> 1];
long long Calc(int l, int r, int k) {
    if (k == 0) return 0;
    if (l > r) return -1e15;
    long long &res = f[l][r][k];
    if (res != -1) return res;
    res = max(Calc(l + 1, r, k), Calc(l, r - 1, k));
    if (l <= r - 1) {
        res = max(res, Calc(l, r - 2, k - 1) + abs(a[r] - a[r - 1]));
        res = max(res, Calc(l + 2, r, k - 1) + abs(a[l] - a[l + 1]));
        res = max(res, Calc(l + 1, r - 1, k - 1) + abs(a[l] - a[r]));
    }
    return res;
}
int main() {
#ifdef LDT
    freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
#else
    freopen("BONUS.INP", "r", stdin);
    freopen("BONUS.OUT", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> k;
    for (int i = 1; i <= n; ++i) cin >> a[i];
    memset(f, 255, sizeof(f));
    cout << Calc(1, n, k);
    return 0;
}