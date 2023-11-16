#include<iostream>
using namespace std;
class Final
{
    private:
        int a,b;
    public:
          Final()
          {
            cin>>a;
            b=a;
            cout<<b;
          }
          ~Final()
          {
            
          }
};

int main()
{
    Final f;
    return 0;
}