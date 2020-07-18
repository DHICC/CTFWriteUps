#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef set<int> si;
typedef set<ll> sll;
typedef pair<int,int> pi;
 
#define F first
#define S second
#define PB push_back
#define INS insert
#define MP make_pair
 
#define LOOP(i,a,b) for (ll i = a; i < b; i++)
#define REVL(i,a,b) for (ll i = a; i --> b; )
#define INTOI(i) int i; cin >> i
#define INTOLL(i) ll i; cin >> i
 
int main()
{
    INTOLL(t);
    while(t--) {
        vll v;
        INTOLL(c);
 
        LOOP(i, 0, c) {
            INTOLL(a);
            v.PB(a);
        }
 
        ll foot = v[c-1];
        bool up = true;
 
        if(c == 1) {
            cout << 0 << "\n";
        }
 
        REVL(i,c - 1,0){
            if(up == false and v[i] > foot) {
                cout << i + 1 << "\n";
                break;
            } else if (up == true and v[i] < foot) {
                foot = v[i];
                up = false;
            }
 
            if(i == 0) {
                cout << 0 << "\n";
                break;
            }
            
            foot = v[i];
        }
 
        v.clear();
    }
}
