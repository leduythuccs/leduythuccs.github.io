#include <bits/stdc++.h>

using namespace std;
const int base = 3;
vector<vector<int> > a, f;
vector<vector<pair<int, int> > > oper;
int n, m, k;
int solve(int target) {
    int res = 0;
    f = vector<vector<int> > (m + 2, vector<int> (n + 2, 0));
    for (int i = 1; i <= m; ++i)
        for (int j = 1; j <= n; ++j) {
            f[i][j] += f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1];
            f[i][j] %= base;
            if (f[i][j] < 0) f[i][j] += base;
            int current = a[i][j] + f[i][j];
            current %= base;
            if (current < 0) current += base;
            if (current == target) continue;
            if (oper[i][j].first == 0) return 1e9;
            int x = oper[i][j].first, y = oper[i][j].second;
            int cnt = (target - current + base) % base;
            res += cnt;
            //(i, j) (x, y) += cnt
            f[i][j] += cnt;
            f[i][y + 1] -= cnt;
            f[x + 1][j] -= cnt;
            f[x + 1][y + 1] += cnt;
        }
    return res;
}
int main() {
#ifdef LDT
    freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
#else 
    freopen("LIGHT.INP", "r", stdin);
    freopen("LIGHT.OUT", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> m >> n >> k;
    a = vector<vector<int> > (m + 2, vector<int> (n + 2, 0));
    oper = vector<vector<pair<int, int> > > (m + 2, vector<pair<int, int> > (n + 2, {0, 0}));
    for (int i = 1; i <= m; ++i)
        for (int j = 1; j <= n; ++j)
            cin >> a[i][j];
    for (int i = 1; i <= k; ++i) {
        int r, c, x, y;
        cin >> r >> c >> x >> y;
        assert(oper[r][c].first == 0);
        oper[r][c] = {x, y};
    }
    int res = min(solve(1), solve(2));
    if (res > 1e8) res = -1;
    cout << res;
    return 0;
}