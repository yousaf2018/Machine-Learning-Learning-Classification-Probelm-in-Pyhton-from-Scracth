#class for machine learning probelm classification 
class AI_model():
    #Training data with x,y,outputlabel
    training_data = [[1,1,1],[9.4,6.4,1],[2.5,2.1,1],[8,7.7,-1],[0.5,2.2,-1],[7.9,8.4,-1],[7,7,-1],[2.8,0.8,1],[1.2,3,-1],[7.8,6.1,1]]
    #Initial weights for machine learning model
    w_old = [-1, -1, -1]
    #Learning rate
    l_r = 0.02
    #function for prediction on basis on input x,y
    def activated_function(self,index):
        w1_x = self.w_old[0] * self.training_data[index][0]
        w2_y = self.w_old[1] * self.training_data[index][1]
        wo_x0 = self.w_old[2] * 1
        sum = w1_x + w2_y + wo_x0
        if sum >= 0:
            return 1
        else:
            return -1
    def learning(self,index,Actual):
        self.w_old[0] = self.w_old[0] + self.l_r*(self.training_data[index][2]-Actual)*self.training_data[index][0]
        self.w_old[1] = self.w_old[1] + self.l_r*(self.training_data[index][2]-Actual)*self.training_data[index][1]
        self.w_old[2] = self.w_old[2] + self.l_r*(self.training_data[index][2]-Actual)*self.training_data[index][2]
if __name__ == "__main__":
    AI_model = AI_model()
    #30 epocchs for training
    for j in range(30):
        print("**************************************************")
        for i in range(len(AI_model.training_data)):
            check = AI_model.activated_function(i)
            if AI_model.training_data[i][2] == check:
                print("Hi")
            else:
                AI_model.learning(i,check)
                print("Happy Learning")
        print("**************************************************")


