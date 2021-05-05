# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
def LoadData(
    OriFile = 'C:\\Users\\wondering\\Desktop\\syl_thesis\\DATA\\dataOri.xls',
    date = ['0530','0609','0624','0725','0826','0925'],
    DateRanges = [5,31,51,77,104,130],
    TypeRanges = [2,5,8,11,14,17,20],
    NumControl = 4):
    """
    res = [Type, date, Control]

    # 1 Total Labile Pi(mg/L)
    # 2 Total Labile Pi(mg/kg)
    # 4 Labile Pi(mg/L)
    # 5 Labile Pi(mg/kg)
    # 7 Labile Po(mg/L)
    # 8 Labile Po(mg/kg)
    # 10 Ca Mg-P(mg/L)
    # 11 Ca Mg-P(mg/kg)
    # 13 Fe Lv-P(mg/L)
    # 14 Fe Lv-P(mg/kg)
    # 16 微生物P(mg/L)	
    # 17 微生物P(mg/kg)
    # 19 腐殖酸-P(mg/L)	
    # 20 腐殖酸-P(mg/kg)
    """
    
    

    data = pd.read_excel(OriFile)
    content = data.values

    res = np.zeros((len(TypeRanges),len(date),NumControl))
    for IndexType in range(len(TypeRanges)) :
        for IndexDate in range(len(date)):
            if IndexDate == 1:
                ControlGroup = 2
            else:
                ControlGroup = 3
            Step = - ControlGroup
            for IndexControl in range(NumControl):
                
                if IndexControl != 3:
                    Step = Step + ControlGroup
                else:
                    Step = Step + ControlGroup * 4
                
                
                x = DateRanges[IndexDate]-2+Step
                y = TypeRanges[IndexType]
                res[IndexType,IndexDate,IndexControl] = np.average(np.array(content[x:x+ControlGroup,y],dtype=float))
                # print(np.average(np.array(content[x:x+ControlGroup,y],dtype=float)))
                # print('--------')
                

        
        # work_book=xlwt.Workbook(encoding='utf-8')
        
        # sheet=work_book.add_sheet('sheet表名')
        # work_book.save(''.join([FileFolder,datenow,'.xls']))
        # workbook = xlrd.open_workbook(''.join([FileFolder,datenow,'.xls']))
        # sheet = workbook.sheet_by_name('sheet表名')
    return res
def PlotTime(Res,
    date = [0,10,25,56,88,118],
    TypeRanges = [2,5,8,11,14,17,20],
    NumControl = 4,
    figsize =  (12,18)
    ):
    """
        This function is used for ploting the different kinds of P in various time

        res = [Type, date, Control]
        date = ['0530','0609','0624','0725','0826','0925']
    """
    settings = {'markersize':10,'linewidth' : 0.6}
    font1 = {'family' : 'Times New Roman',
    'weight' : 'normal',
    'size'   : 20,
    }
    title = (
    'Total Labile Pi(mg/kg)'
    ,'Labile Pi(mg/kg)',
    'Labile Po(mg/kg)',
    'Ca Mg-P(mg/kg)',
    'Fe Al-P(mg/kg)',
    'Ml-Po(mg/kg)',
    'Hu-P(mg/kg)')
    TextControl = ('$NB_5$','$NB_{10}$','$B_{20}$','$N$')
    PlotStyle = ('*-','v-','s-','o-')
    NumType = len(TypeRanges)
    fig, ax = plt.subplots(6, 1, figsize=figsize)
    # plt.subplots_adjust(hspace=1, wspace=3)
    for i in range(1,NumType):
        # ax = plt.subplot(6,1,i)
        
        for j in range(NumControl):
            ax[i-1].plot(date,Res[i,:,j],PlotStyle[j],**settings)
        ax[i-1].legend(TextControl)
        ax[i-1].set_ylabel(title[i],font1)
        # plt.ylabel(title[i],font1)
        ax[i-1].set_xticks(date)
        if i > 5:
            ax[i-1].set_xlabel('Time / day',font1)
            # plt.xlabel('Time / day',font1)
        # 设置坐标刻度值的大小以及刻度值的字体
        ax[i-1].tick_params(labelsize=font1['size'])
        labels = ax[i-1].get_xticklabels() + ax[i-1].get_yticklabels()
        # print labels
        [label.set_fontname('Times New Roman') for label in labels]
    plt.show()
    plt.savefig("TimeIndividual", bbox_inches="tight")
def PlotPie(Res,
    date = [0,10,25,56,88,118],
    TypeRanges = [2,5,8,11,14,17,20],
    NumControl = 4,
    figsize =  (20,20),
    DatePlot = 4,
    ):
    """
        This function is used for ploting the different kinds of P in various time

        res = [Type, date, Control]
        date = ['0530','0609','0624','0725','0826','0925']
    """
    settings = {}
    font1 = {'family' : 'Times New Roman',
    'weight' : 'normal',
    'size'   : 20,
    }
    title = (
        'Labile Pi',
        'Labile Po',
        'Ca Mg-P',
        'Fe Al-P',
        'Ml-Po',
        'Hu-P')
    TextControl = ('$NB_5$','$NB_{10}$','$B_{20}$','$N$')
    NumType = len(TypeRanges)
    fig, ax = plt.subplots(2, 2, figsize=figsize)
    # plt.subplots_adjust(hspace=1, wspace=3)
    ax = ax.reshape((4))
    explode = np.zeros(len(title))
    explode[2] += 0.1
    for j in range(NumControl):
        ax[j].pie(Res[1:,DatePlot,j],labels=title,
            autopct='%1.1f%%',
            explode = explode,
            shadow=True,textprops = font1,**settings)
        ax[j].set_title(TextControl[j],font1)

        # 设置坐标刻度值的大小以及刻度值的字体
        ax[j].tick_params(labelsize=font1['size'])
        labels = ax[j].get_xticklabels() + ax[j].get_yticklabels()
        # print labels
        [label.set_fontname('Times New Roman') for label in labels]
    plt.show()

if __name__ == '__main__':
    res = LoadData()
    # PlotTime(res)
    PlotPie(res)