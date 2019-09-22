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
  string s;
  string t;
  std::cin >> s >> t;
  int minNumber = n;
  vector<int> minPlaces;
  for (int i = 0; i < n; i++) {
    minPlaces.push_back(i+1);
  }
  for (int i = 0; i < m-n+1; i++) {
    int curNumber;
    vector<int> curPlaces;
    curNumber = 0;
    for (int j = 0; j < n; j++) {
      if (s[j] != t[i+j]) {
	curNumber += 1;
	curPlaces.push_back(j+1);
      }
    }
    if (curNumber < minNumber) {
      minNumber = curNumber;
      minPlaces = curPlaces;
      minPlaces.resize(minNumber);
      minPlaces.shrink_to_fit();
    }
  }
  std::cout << minNumber << "\n";
  if (not minPlaces.empty()) {
    std::cout << minPlaces[0];
    for (int i = 1; i < minPlaces.size(); i++) {
      std::cout << " " << minPlaces[i];
    }
    std::cout << "\n";
  }
  return 0;
}
