#include <iostream>
#include <random>
#include <chrono>
using namespace std;


/**struct vector {
    double x;
    double y;
    double z;

};

class NoiseRW_Avg(vector mean,
                  vector stdev,
                  double time_forward,
                  int num_grid_points)
    : m_mean(mean),
      m_stdev(stdev),
      m_time_forward(time_forward),
      m_num_grid_points(num_grid_points){

    } 
**/
//Generates a mean for a normal distribution relative to concentration gradient. The maxD is the maximum range (distance from mean) we want to allow the measurement
//to get, and the maxR is the maximum shift in mean we want to allow.
double nudge (double meas, double maxR, double maxD){
    double myNudge = -meas/maxD;
    if(abs(myNudge) >= maxR) myNudge = maxR*((myNudge>0)-(myNudge<0));
    return myNudge;
}
void RandomWalk(double* meas, double* dmeas, int steps, double rand){

    //initiate a bunch of constants. In the future, these will need to be passed in to the function. via some GPS model.
    double sigma = 0.016289174978068626;
    double maxv = 0.03;
    double maxNudge = sigma*0.2;
    double maxa = 0.005;
    double n = maxNudge*nudge(*meas, 1, 1);
    double a = rand+n;
    //cout << "a is: " << a << "\n";

    //Make a the maximum value it is allowed to be, while maintaining it's sign.
    if(abs(a)>maxa) a = maxa*((a > 0) - (a < 0));


    *meas = *meas+*dmeas+a;
    *dmeas = *dmeas+a;
    if(abs(*dmeas)>maxv) *dmeas = maxv * ((*dmeas > 0) - (*dmeas < 0));
}

int main(){
    double* meas = NULL;
    double* dmeas = NULL;
    double b = 0;
    double c = 0;
    meas = &b;
    dmeas = &c;
    double sigma = 0.016289174978068626;
    std::default_random_engine generator;
    std::normal_distribution<double> distribution(0, sigma);
    for(int i = 0;i<1000;i++){
        double rand = distribution(generator);

        RandomWalk(meas, dmeas, 1, rand);
        cout << *meas<<"\n";
    }
    return 0;
}