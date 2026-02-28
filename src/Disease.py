#Disease Class: Mo Spiegel, Period 3B

import random

class Disease:
    
    #Class Attributes: Lists of all possible symptoms, progressing in severity
    symptomsTier1 = ["上火 (Shànghuǒ)","气虚 (Qì Xū)","肝气郁结 (Gān Qì Yù Jié)", "风寒 (Fēng Hán)"] 
    symptomsTier2 = ["痰湿 (Tán Shī)","湿热 (Shī Rè)","风热 (Fēng Rè)"]
    symptomsTier3 = ["阳虚 (Yáng Xū)","阴虚 (Yīn Xū)","血瘀 (Xuè Yū)"]
   
    def __init__(self, year, severityIndex, symptoms, nodeCoord, area, cured):
        self.year = year #Takes year count from main file
        self.severityIndex = 0 #Modified by 'getSeverityIndex' method
        self.symptoms = [] #Modified by 'getSymptoms' method
        self.nodeCoord = (random.randint(), random.randint()) #Will be generated within map range: Denotes starting point of disease
        self.area = [] #List of coordinates where the disease exists
        self.cured = False

    def getSymptoms(self):
        if self.year <= 80:
            x = random.randint(1,3) #Denotes how many symptoms will be present in an instance of a disease (bounds increase with time)
            tempList1 = Disease.symptomsTier1 #Creates a temporary list that will be edited
        elif self.year <= 200:
            x = random.randint(1,4)
            tempList1 = Disease.symptomsTier1
            tempList2 = Disease.symptomsTier2 #Higher tier symptoms occur as time continues
        elif self.year <= 500:
            x = random.randint(1,5)
            tempList1 = Disease.symptomsTier1
            tempList2 = Disease.symptomsTier2
            tempList3 = Disease.symptomsTier3
        elif self.year <= 500:
            x = random.randint(1,5)
            tempList1 = Disease.symptomsTier1
            tempList2 = Disease.symptomsTier2
            tempList3 = Disease.symptomsTier3        
            
        while x > 0:
            #Appends symptoms randomly chosen from each existing tier to the symptoms list, symptoms appended until the disease has x symptoms
            if tempList1 != []:
                symp = tempList1[random.randint(0,len(tempList1)-1)]
                self.symptoms.append(symp)
                tempList1.remove(symp)
                x = x - 1
                if x == 0:
                    break
            if tempList2 != []: 
                symp = tempList2[random.randint(0,len(tempList2)-1)]
                self.symptoms.append(symp)
                tempList2.remove(symp)
                x = x - 1
                if x == 0:
                    break
            if tempList3 != []: 
                symp = tempList3[random.randint(0,len(tempList3)-1)]
                self.symptoms.append(symp)
                tempList3.remove(symp)
                x = x - 1
                if x == 0:
                    break
        
    def getSeverityIndex(self):
        for i in self.symptoms:
            #Assigns each symptom of the disease a severity index based on its tier
            #The sum of each symptoms' severity index is the disease severity 
            if i == "上火 (Shànghuǒ)":
                shanghuoSev = random.randint(1,4)
                self.severity = self.severity + shanghuoSev
                
            elif i == "气虚 (Qì Xū)":
                qixuSev = random.randint(1,4)
                self.severity = self.severity + qixuSev
                               
            elif i == "肝气郁结 (Gān Qì Yù Jié)":
                ganqiyujieSev = random.randint(1,4)
                self.severity = self.severity + ganqiyujieSev

            elif i == "风寒 (Fēng Hán)":
                fenghanSev = random.randint(1,4)
                self.severity = self.severity + fenghanSev
                
            elif i == "痰湿 (Tán Shī)":
                tanshiSev = random.randint(2,5)
                self.severity = self.severity + tanshiSev
                
            elif i == "湿热 (Shī Rè)":
                shireSev = random.randint(2,5)
                self.severity = self.severity + shireSev
                
            elif i == "风热 (Fēng Rè)":
                fengreSev = random.randint(2,5)          
                self.severity = self.severity + fengreSev
      
            elif i == "阳虚 (Yáng Xū)":
                yangxuSev = random.randint(3,6)               
                self.severity = self.severity + yangxuSev

            elif i == "阴虚 (Yīn Xū)":
                yinxuSev = random.randint(3,6)               
                self.severity = self.severity + yinxuSev
                
            elif i == "血瘀 (Xuè Yū)":
                xueyuSev = random.randint(3,6)               
                self.severity = self.severity + xueyuSev    
                
    def spread(self):
        #Called every time a year/tick passes, adds more afflicted coordinates to the area list by increasing severity
        pass

    def cure(self, medicines):
        #The presence of a pharmacy will call the cure method and pass in the list of medicines the pharmacy has, which will decrease the severity of symptoms
        pass
    
    def end(self):
        if self.severity == 0:
            self.cured = True
            return self.cured
            



