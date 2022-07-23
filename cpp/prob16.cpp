
#include <iostream>
#include <algorithm>
using namespace std;


int N;
int A, B, C;

int main() {
	cin >> N;
	cin >> A >> B >> C;

	// long long Answer = (1LL << 30);

    int minCoin = min(A, min(B, C));
    cout << minCoin << endl;
    std::vector<int> dp(N+1, 0);
    dp[A] =  dp[B] = dp[C] = 1;
    for (int i=minCoin; i<=N; i++){
        dp[i] = min(dp[i-A], min(dp[i-B], dp[i-C]));
    }

	cout << dp[N] << endl;
	return 0;
}