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

using namespace std;

int main()
{
  ios::sync_with_stdio(false);
  std::cin.tie(0);
  int n;
  int m;
  std::cin >> n >> m;
  string cells[n];
  for (int i = 0; i < n; i++) {
    std::cin >> cells[i];
  }
  bool possible = true;
  int rightColumn = -1;
  int bottomRow = -1;
  int leftColumn = -1;
  int topRow = -1;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if ('B' == cells[j][m-i-1])
	leftColumn = m-i-1;
      if ('B' == cells[j][i])
	rightColumn = i;
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if ('B' == cells[i][j])
	bottomRow = i;
      if ('B' == cells[n-i-1][j])
	topRow = n-i-1;
    }
  }
  int sidelength = max(rightColumn-leftColumn+1, bottomRow-topRow+1);
  int ans = sidelength*sidelength;
  if (-1 == topRow)
    ans = 1;
  if ((sidelength > n) or (sidelength > m))
    possible = false;
  for (int i = topRow; i < bottomRow+1; i++) {
    for (int j = leftColumn; j < rightColumn+1; j++) {
      if ('B' == cells[i][j])
	ans -= 1;
    }
  }
  if (possible)
    std::cout << ans << "\n";
  else
    std::cout << "-1\n";
  return 0;
}
