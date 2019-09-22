#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>

#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  int n;
  int m;
  std::cin >> n >> m;
  vector<double> dormsizes;
  for (int i = 0; i < n; i++) {
    double cur;
    std::cin >> cur;
    dormsizes.push_back(cur);
  }
  vector<double> letters;
  for (int i = 0; i < m; i++) {
    double cur;
    std::cin >> cur;
    letters.push_back(cur);
  }
  int dorm = 0;
  double rooms = 0;
  std::cout << setprecision(16);
  for (int i = 0; i < m; i++) {
    while (rooms+dormsizes[dorm] < letters[i]) {
      rooms += dormsizes[dorm];
      dorm += 1;
    }
    std::cout << dorm+1 << " " << letters[i]-rooms << "\n";
  }
  return 0;
}
