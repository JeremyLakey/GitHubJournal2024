class Solution {
public:
    vector<double> sampleStats(vector<int>& count) {

        double min = -1;
        double max = -1;   
        long total = 0;
        
        long c = 0;
        long mode = -1;
        long modeCount = 0;


        for (int i = 0; i < count.size(); i++) {
            total += count.at(i) * (long)i;
            c += count.at(i);

            if(count.at(i) > 0) {
                if (min == -1) {
                    min = i;
                }
                max = i;

                if (modeCount < count.at(i)) {
                    modeCount = count.at(i);
                    mode = i;
                }
            }
        }

        float median = 0.0;
        if (c % 2 == 1) {
            int temp = (c / 2) + 1;
            for(int i = 0; i < count.size(); i++) {
                temp -= count.at(i);
                if (temp <= 0) {
                    median = (float)i;
                    break;
                }
            }
        }
        else {
            int temp = c / 2;
            for(int i = 0; i < count.size(); i++) {
                temp -= count.at(i);
                if (temp == 0) {
                    median = i;
                    for (int j = i + 1; j < count.size(); j++) {
                        if (count.at(j) > 0) {
                            median = (median + j) / 2;
                            break;
                        }
                    }
                    break;
                }
                if (temp < 0) {
                    median = i;
                    break;
                }
            }
        }

        double mean = ((double)total)/(c);
        vector<double> stats;

        stats.push_back(min);
        stats.push_back(max);
        stats.push_back(mean);
        stats.push_back(median);
        stats.push_back((double)mode);
        return stats;
    }
};