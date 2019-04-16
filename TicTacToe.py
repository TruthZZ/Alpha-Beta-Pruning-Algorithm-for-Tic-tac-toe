import sys;
import numpy as np;
from PyQt5.QtWidgets import *;
from PyQt5.QtGui import *;

class HeuristicTTT:
    def __init__(self,Dimention,cmap,sidevalue):
        super().__init__();
        self.initTTToe(Dimention,cmap,sidevalue);


    def initTTToe(self,Dimention,cmap,sidevalue):
        self.Dimention = Dimention;
        self.cmap = cmap;
        self.sidevalue = sidevalue;


    def CalStepGain(self,R,C,cmap):
        stepGain = 0;
        tempmap = cmap;
        if self.sidevalue == 1:
            myside = 1;
            enemy = -1;
        elif self.sidevalue == -1:
            myside = -1;
            enemy = 1;

        if (sum((tempmap[R,i]==1) for i in range(self.Dimention)) != 0)and(sum((tempmap[R,i]==-1) for i in range(self.Dimention)) != 0):
            stepGain = stepGain;
        elif (sum((tempmap[R,i]==1) for i in range(self.Dimention)) == 0)and(sum((tempmap[R,i]==-1) for i in range(self.Dimention)) == 0):
            stepGain = stepGain + 1;
        elif (sum((tempmap[R,i]==enemy) for i in range(self.Dimention)) == 0):
            compnum = sum((tempmap[R,i] == myside) for i in range(self.Dimention));
            if compnum == (self.Dimention-1):
                compnum = compnum*3;
            stepGain = stepGain + compnum + 1;
        elif (sum((tempmap[R,i]==myside) for i in range(self.Dimention)) == 0):
            destnum = sum((tempmap[R,i] == enemy) for i in range(self.Dimention));
            if destnum == (self.Dimention-1):
                destnum = destnum*2;
            stepGain = stepGain + destnum + 1;


        if (sum((tempmap[i,C]==1) for i in range(self.Dimention)) != 0)and(sum((tempmap[i,C]==-1) for i in range(self.Dimention)) != 0):
            stepGain = stepGain;
        elif (sum((tempmap[i,C]==1) for i in range(self.Dimention)) == 0)and(sum((tempmap[i,C]==-1) for i in range(self.Dimention)) == 0):
            stepGain = stepGain + 1;
        elif (sum((tempmap[i,C]==enemy) for i in range(self.Dimention)) == 0):
            compnum = sum((tempmap[i,C] == myside) for i in range(self.Dimention));
            if compnum == (self.Dimention-1):
                compnum = compnum*3;
            stepGain = stepGain + compnum + 1;
        elif (sum((tempmap[i,C]==myside) for i in range(self.Dimention)) == 0):
            destnum = sum((tempmap[i,C] == enemy) for i in range(self.Dimention));
            if destnum == (self.Dimention-1):
                destnum = destnum*2;
            stepGain = stepGain + destnum + 1;


        if R == C:
            if (sum((tempmap[i,i]==1) for i in range(self.Dimention)) != 0)and(sum((tempmap[i,i]==-1) for i in range(self.Dimention)) != 0):
                stepGain = stepGain;
            elif (sum((tempmap[i,i]==1) for i in range(self.Dimention)) == 0)and(sum((tempmap[i,i]==-1) for i in range(self.Dimention)) == 0):
                stepGain = stepGain + 1;
            elif (sum((tempmap[i,i]==enemy) for i in range(self.Dimention)) == 0):
                compnum = sum((tempmap[i,i] == myside) for i in range(self.Dimention));
                if compnum == (self.Dimention-1):
                    compnum = compnum*3;
                stepGain = stepGain + compnum + 1;
            elif (sum((tempmap[i,i]==myside) for i in range(self.Dimention)) == 0):
                destnum = sum((tempmap[i,i] == enemy) for i in range(self.Dimention));
                if destnum == (self.Dimention-1):
                    destnum = destnum*2;
                stepGain = stepGain + destnum + 1;


        if R+C == (self.Dimention-1):
            if (sum((tempmap[i,self.Dimention-i-1]==1) for i in range(self.Dimention)) != 0)and(sum((tempmap[i,self.Dimention-i-1]==-1) for i in range(self.Dimention)) != 0):
                stepGain = stepGain;
            elif (sum((tempmap[i,self.Dimention-i-1]==1) for i in range(self.Dimention)) == 0)and(sum((tempmap[i,self.Dimention-i-1]==-1) for i in range(self.Dimention)) == 0):
                stepGain = stepGain + 1;
            elif (sum((tempmap[i,self.Dimention-i-1]==enemy) for i in range(self.Dimention)) == 0):
                compnum = sum((tempmap[i,self.Dimention-i-1] == myside) for i in range(self.Dimention));
                if compnum == (self.Dimention-1):
                    compnum = compnum*3;
                stepGain = stepGain + compnum + 1;
            elif (sum((tempmap[i,self.Dimention-i-1]==myside) for i in range(self.Dimention)) == 0):
                destnum = sum((tempmap[i,self.Dimention-i-1] == enemy) for i in range(self.Dimention));
                if destnum == (self.Dimention-1):
                    destnum = destnum*2;
                stepGain = stepGain + destnum + 1;

        return stepGain;


    def CalGainMap(self,CurrentMap):
        self.cmap = CurrentMap;
        self.gainmap = np.zeros([self.Dimention,self.Dimention]);

        for i in range(self.Dimention):
            for j in range(self.Dimention):
                if self.cmap[i,j] != 0:
                    self.gainmap[i,j] = -1;
                else:
                    self.gainmap[i,j] = self.CalStepGain(i,j,self.cmap);

        return self.gainmap;

    def mapchanged(self,cmap):
        #print(cmap)
        self.CalGainMap(cmap);
        #print(self.gainmap);
        lindex = np.argmax(self.gainmap);
        #print(lindex)
        x = lindex%self.Dimention;
        y = lindex//self.Dimention;

        return [x,y];


class AlphaBetaTTT:
    def __init__(self,Dimention,cmap,sidevalue):
        super().__init__();
        self.initABCT(Dimention,cmap,sidevalue);

    def initABCT(self,Dimention,cmap,sidevalue):
        self.Dimention = Dimention;
        self.cmap = cmap;
        self.sidevalue = sidevalue;
        self.hfunction = HeuristicTTT(Dimention,cmap,sidevalue);

    def statuscheck(self,cmap):
        game_continue = True;
        game_winner = 0;
        board_full = False;
        empty_num = 0;
        pure_num = 0;
        #print(cmap);

        for R in range(self.Dimention):
            if (sum((cmap[R,j] == 1) for j in range(self.Dimention)) == 0) or (sum((cmap[R,j] == -1) for j in range(self.Dimention)) == 0):
                pure_num = pure_num + 1;

        for C in range(self.Dimention):
            if (sum((cmap[i,C] == 1) for i in range(self.Dimention)) == 0) or (sum((cmap[i,C] == -1) for i in range(self.Dimention)) == 0):
                pure_num = pure_num + 1;

        if (sum((cmap[i,i] == 1) for i in range(self.Dimention)) == 0) or (sum((cmap[i,i] == -1) for i in range(self.Dimention)) == 0):
            pure_num = pure_num + 1;

        if (sum((cmap[i,self.Dimention-i-1] == 1) for i in range(self.Dimention)) == 0) or (sum((cmap[i,self.Dimention-i-1] == -1) for i in range(self.Dimention)) == 0):
            pure_num = pure_num + 1;

        if pure_num == 0:
            game_continue = False;
            game_winner = 0;
            return[game_continue,game_winner];

        for i in range(self.Dimention):
            for j in range(self.Dimention):
                if cmap[i,j] == 0:
                    empty_num = empty_num + 1;
        
        if empty_num == 0:
           board_full = True;
        else:
            board_full = False;

        #print(board_full);

        if bool(1-board_full):
            for R in range(self.Dimention):
                if (sum((cmap[R,j] == 1) for j in range(self.Dimention)) == self.Dimention):
                    game_winner = 1;
                    game_continue = False;
                    return [game_continue,game_winner];
                    break;
                elif (sum((cmap[R,j] == -1) for j in range(self.Dimention)) == self.Dimention):
                    game_winner = -1;
                    game_continue = False;
                    return [game_continue,game_winner];
                    break;
                else:
                    game_winner = 0;
                    game_continue = True;

            for C in range(self.Dimention):
                if sum((cmap[i,C] == 1) for i in range(self.Dimention)) == self.Dimention:
                    game_winner = 1;
                    game_continue = False;
                    return [game_continue,game_winner];
                    break;
                elif sum((cmap[i,C] == -1) for i in range(self.Dimention)) == self.Dimention:
                    game_winner = -1;
                    game_continue = False;
                    return [game_continue,game_winner];
                    break;
                else:
                    game_winner = 0;
                    game_continue = True;

            if sum((cmap[i,i] == 1) for i in range(self.Dimention)) == self.Dimention:
                game_winner = 1;
                game_continue = False;
                return [game_continue,game_winner];
            elif sum((cmap[i,i] == -1) for i in range(self.Dimention)) == self.Dimention:
                game_winner = -1;
                game_continue = False;
                return [game_continue,game_winner];
            else:
                game_winner = 0;
                game_continue = True;

            if sum((cmap[i,self.Dimention-i-1] == 1) for i in range(self.Dimention)) == self.Dimention:
                game_winner = 1;
                game_continue = False;
                return [game_continue,game_winner];
            elif sum((cmap[i,self.Dimention-i-1] == -1) for i in range(self.Dimention)) == self.Dimention:
                game_winner = -1;
                game_continue = False;
                return [game_continue,game_winner];
            else:
                game_winner = 0;
                game_continue = True;

        else:
            game_winner = 0;
            game_continue = False;
            return [game_continue,game_winner];

        return [game_continue,game_winner];

    def mapchanged(self,cmap):
        #print(cmap);
        self.cmap = cmap;
        tempmap0 = np.zeros([self.Dimention,self.Dimention]);
        for i in range(self.Dimention):
            for j in range(self.Dimention):
                tempmap0[i,j] = cmap[i,j];

        #tempmap0 = cmap;
        alphamap0 = np.zeros([self.Dimention,self.Dimention]);
        for i in range(self.Dimention):
            for j in range(self.Dimention):
                alphamap0[i,j] = -2;

        #print('1:')
        #print(cmap);

        betamap = np.zeros([self.Dimention,self.Dimention]);
        for i in range(self.Dimention):
            for j in range(self.Dimention):
                betamap[i,j] = np.inf;

        alphamap1 = np.zeros([self.Dimention,self.Dimention]);

        tempalpha0 = -1;

        for R0 in range(self.Dimention):
            for C0 in range(self.Dimention):
                #tempmap1 = tempmap0;
                tempmap1 = np.zeros([self.Dimention,self.Dimention]);
                for i in range(self.Dimention):
                    for j in range(self.Dimention):
                        tempmap1[i,j] = tempmap0[i,j];

                if tempmap1[R0,C0] != 0:
                    continue;
                else:
                    tempmap1[R0,C0] = self.sidevalue;
                    #print('2:')
                    #print(cmap);
                    betamap = np.zeros([self.Dimention,self.Dimention]);
                    for i in range(self.Dimention):
                        for j in range(self.Dimention):
                            betamap[i,j] = np.inf;

                    caledbetalist = [];
                    tempbeta = np.inf;
                    betacut = False;

                    for R1 in range(self.Dimention):
                        for C1 in range(self.Dimention):
                            #tempmap2 = tempmap1;
                            tempmap2 = np.zeros([self.Dimention,self.Dimention]);
                            for i in range(self.Dimention):
                                for j in range(self.Dimention):
                                    tempmap2[i,j] = tempmap1[i,j];

                            if tempmap2[R1,C1] != 0:
                                thisbeta = np.inf;
                                betamap[R1,C1] = thisbeta;
                                caledbetalist.append(thisbeta);
                                continue;
                            else:
                                #print('enemy move')
                                tempmap2[R1,C1] = -self.sidevalue;
                                #print('add: %d'%(-self.sidevalue));
                                self.cmap = tempmap2;
                                alphamap1 = np.zeros([self.Dimention,self.Dimention]);
                                caledalphalist = [];
                                tempalpha1 = -1;
                                alpha1cut = False;

                                [wincheck,winner] = self.statuscheck(tempmap2);
                                enemywin = bool(1-wincheck) and (winner != 0);
                                #print(tempmap2);
                                #print([R0,C0,R1,C1]);
                                #print(self.cmap);
                                #print('ABC: wincheck: %s'%(wincheck));
                                if enemywin == True:
                                    thisbeta = -np.inf;
                                else:
                                    for R2 in range(self.Dimention):
                                        for C2 in range(self.Dimention):
                                            #tempmap3 = tempmap2;
                                            tempmap3 = np.zeros([self.Dimention,self.Dimention]);
                                            for i in range(self.Dimention):
                                                for j in range(self.Dimention):
                                                    tempmap3[i,j] = tempmap2[i,j];

                                            if tempmap3[R2,C2] != 0:
                                                thisalpha1 = -1;
                                                alphamap1[R2,C2] = thisalpha1;
                                                caledalphalist.append(thisalpha1);
                                                #print(len(caledalphalist));
                                                continue;
                                            else:
                                                thisalpha1 = self.hfunction.CalStepGain(R2,C2,tempmap3);
                                                alphamap1[R2,C2] = thisalpha1;
                                                caledalphalist.append(thisalpha1);
                                                #print(len(caledalphalist))

                                            if thisalpha1 > tempalpha1:
                                                tempalpha1 = thisalpha1;

                                            if tempalpha1 > tempbeta:
                                                alpha1cut = True;
                                                break;

                                        if alpha1cut:
                                            break;

                                if enemywin == True:
                                    thisbeta = -np.inf;
                                    print(thisbeta);
                                else:
                                    thisbeta = max(caledalphalist);
                                wincheck = True;
                                betamap[R1,C1] = thisbeta;
                                caledbetalist.append(thisbeta);
                                #print(len(caledalphalist));
                                if thisbeta < tempbeta:
                                    tempbeta = thisbeta;

                                if tempbeta < tempalpha0:
                                    betacut = True;
                                    break;

                            if betacut:
                                break;

                    thisalpha0 = min(caledbetalist);
                    alphamap0[R0,C0] = thisalpha0;

        lindex = np.argmax(alphamap0);
        #print(alphamap0);
        x = lindex%self.Dimention;
        y = lindex//self.Dimention;
        #print([x,y])

        return [x,y];


class TTToeView(QWidget):
    def __init__(self):
        super().__init__();
        self.initUI();

    def initUI(self):
        self.setGeometry(100,50,800,800);
        self.setWindowTitle('Tic-Tac-Teo');
        self.setVisible(True);

        Headwidth = 50;
        Leftwidth = 50;
        self.lattice_list = [];

        self.title_label = QLabel('一字棋',self);
        self.title_label.setGeometry(Leftwidth,Headwidth,100,20);
        self.title_label.setVisible(True);

        self.length_label = QLabel('设置长度：',self);
        self.length_label.setGeometry(Leftwidth+20,Headwidth+50,100,20);
        self.length_label.setVisible(True);

        self.length_text = QLineEdit(self);
        self.length_text.setGeometry(Leftwidth+120,Headwidth+50,100,20);
        self.length_text.setVisible(True);

        self.player1_label = QLabel('玩家x:(先手)',self);
        self.player1_label.setGeometry(Leftwidth+20,Headwidth+100,100,20);
        self.player1_label.setVisible(True);

        self.player2_label = QLabel('玩家o:(后手)',self);
        self.player2_label.setGeometry(Leftwidth+140,Headwidth+100,80,20);
        self.player2_label.setVisible(True);

        self.vs_label = QLabel('vs',self);
        self.vs_label.setGeometry(Leftwidth+105,Headwidth+110,100,20);
        self.vs_label.setVisible(True);

        self.players = ['玩家','爬山法','α-β剪枝'];

        self.player1_combox = QComboBox(self);
        self.player1_combox.addItems(self.players);
        self.player1_combox.setGeometry(Leftwidth+20,Headwidth+120,60,20);
        self.player1_combox.setVisible(True);

        self.player2_combox = QComboBox(self);
        self.player2_combox.addItems(self.players);
        self.player2_combox.setGeometry(Leftwidth+140,Headwidth+120,80,20);
        self.player2_combox.setVisible(True);

        #self.first_label = QLabel('选择先手：',self);
        #self.first_label.setGeometry(Leftwidth+20,Headwidth+175,100,20);
        #self.first_label.setVisible(True);

        #self.firsts = ['玩家1','玩家2'];
        #self.first_combox = QComboBox(self);
        #self.first_combox.addItems(self.firsts);
        #self.first_combox.setGeometry(Leftwidth+120,Headwidth+175,100,20);
        #self.first_combox.setVisible(True);

        self.start_button = QPushButton('开始',self);
        self.start_button.setGeometry(Leftwidth+20,725,100,50);
        self.start_button.clicked.connect(lambda:self.start());
        self.start_button.setVisible(True);

    def start(self):
        self.getparam();
        self.cmap = np.zeros([self.winlength,self.winlength]);
        self.HeuSolution = HeuristicTTT(self.winlength,self.cmap,self.AIvalue);
        self.ABCSolution = AlphaBetaTTT(self.winlength,self.cmap,self.AIvalue);

        self.AItwoh = False;

        if bool(1-self.human1bool):
            if self.player1_ind == 1:
                self.AIsolution1 = self.HeuSolution;
            elif self.player1_ind == 2:
                self.AIsolution1 = self.ABCSolution;

        if bool(1-self.human2bool):
            if self.player2_ind == 1:
                self.AItwoh = True;
                self.AIsolution2 = self.HeuSolution;
            elif self.player2_ind == 2:
                self.AIsolution2 = self.ABCSolution;

        if bool(1-self.twoAI) and bool(1-self.twohuman):
            if self.humanfirst:
                self.AISolution = self.AIsolution2;
            else:
                self.AISolution = self.AIsolution1;

        if self.twoAI:
            if self.AItwoh:
                self.AIsolution2.sidevalue = -self.AIsolution2.sidevalue;
                print('changed! %d %d'%(self.AIsolution1.sidevalue,self.AIsolution2.sidevalue));

            self.AISolution = self.AIsolution1;
            self.AItag = 1;

        board_x = 400;
        board_y = 100;
        lattice_width = 50;

        if len(self.lattice_list) != 0:
            for lattice in self.lattice_list:
                lattice.lbutton.deleteLater();
            self.lattice_list = [];

        for i in range(self.winlength):
            for j in range(self.winlength):
                templattice = Lattice(j,i,self);
                templattice.setGeometry(board_x+j*lattice_width,board_y+i*lattice_width,lattice_width,lattice_width);
                self.lattice_list.append(templattice);

        if bool(1-self.humanfirst):
            self.mapchanged(True);

    def getparam(self):
        self.winlength = int(self.length_text.text());
        self.player1_ind = self.player1_combox.currentIndex();
        self.player2_ind = self.player2_combox.currentIndex();
        #self.firsthand = self.first_combox.currentIndex();

        #if self.firsthand == 0:
        #    self.handbool = True;
        #elif self.firsthand == 1:
        #    self.handbool = False;

        if self.player1_ind == 0:
            self.human1bool = True;
        else:
            self.human1bool = False;

        if self.player2_ind == 0:
            self.human2bool = True;
        else:
            self.human2bool = False;

        self.humanfirst = self.human1bool;
        self.twohuman = self.human1bool and self.human2bool;
        self.twoAI = bool(1-self.human1bool) and bool(1-self.human2bool);

        if bool(1-self.humanfirst):
            self.AIvalue = 1;
        else:
            self.AIvalue = -1;

    def AImove(self,x,y):
        latticeindex = y*self.winlength + x;
        targetlattice = self.lattice_list[latticeindex];
        targetlattice.AImove(self);

    def mapchanged(self,humanflag):
        #print(humanflag)
        #print(self.cmap);
        #print(self.cmap)
        if bool(1-self.twohuman) and humanflag:
            [x,y] = self.AISolution.mapchanged(self.cmap);
            #print('move twice!1111: %s'%(humanflag));
            self.AImove(x,y);
        elif self.twoAI:
            print('AITag: %d'%(self.AItag));
            [x,y] = self.AISolution.mapchanged(self.cmap);
            #print('move twice!2222')
            self.AIswitch();
            self.AImove(x,y);

    def AIswitch(self):
        if self.AItag == 1:
            print('switch to 2')
            self.AISolution = self.AIsolution2;
            self.AItag = 2;
        elif self.AItag == 2:
            print('switch to 1')
            self.AISolution = self.AIsolution1;
            self.AItag = 1;

    def statuscheck(self):
        game_continue = True;
        game_winner = 0;
        board_full = False;
        empty_num = 0;
        pure_num = 0;

        for R in range(self.winlength):
            if (sum((self.cmap[R,j] == 1) for j in range(self.winlength)) == 0) or (sum((self.cmap[R,j] == -1) for j in range(self.winlength)) == 0):
                pure_num = pure_num + 1;

        for C in range(self.winlength):
            if (sum((self.cmap[i,C] == 1) for i in range(self.winlength)) == 0) or (sum((self.cmap[i,C] == -1) for i in range(self.winlength)) == 0):
                pure_num = pure_num + 1;

        if (sum((self.cmap[i,i] == 1) for i in range(self.winlength)) == 0) or (sum((self.cmap[i,i] == -1) for i in range(self.winlength)) == 0):
            pure_num = pure_num + 1;

        if (sum((self.cmap[i,self.winlength-i-1] == 1) for i in range(self.winlength)) == 0) or (sum((self.cmap[i,self.winlength-i-1] == -1) for i in range(self.winlength)) == 0):
            pure_num = pure_num + 1;

        if pure_num == 0:
            game_continue = False;
            game_winner = 0;
            return[game_continue,game_winner];

        for i in range(self.winlength):
            for j in range(self.winlength):
                if self.cmap[i,j] == 0:
                    empty_num = empty_num + 1;
        
        if empty_num == 0:
           board_full = True;
        else:
            board_full = False;

        #print(board_full);

        if bool(1-board_full):
            for R in range(self.winlength):
                if (sum((self.cmap[R,j] == 1) for j in range(self.winlength)) == self.winlength):
                    game_winner = 1;
                    game_continue = False;
                    return [game_continue,game_winner];
                    break;
                elif (sum((self.cmap[R,j] == -1) for j in range(self.winlength)) == self.winlength):
                    game_winner = -1;
                    game_continue = False;
                    return [game_continue,game_winner];
                    break;
                else:
                    game_winner = 0;
                    game_continue = True;

            for C in range(self.winlength):
                if sum((self.cmap[i,C] == 1) for i in range(self.winlength)) == self.winlength:
                    game_winner = 1;
                    game_continue = False;
                    return [game_continue,game_winner];
                    break;
                elif sum((self.cmap[i,C] == -1) for i in range(self.winlength)) == self.winlength:
                    game_winner = -1;
                    game_continue = False;
                    return [game_continue,game_winner];
                    break;
                else:
                    game_winner = 0;
                    game_continue = True;

            if sum((self.cmap[i,i] == 1) for i in range(self.winlength)) == self.winlength:
                game_winner = 1;
                game_continue = False;
                return [game_continue,game_winner];
            elif sum((self.cmap[i,i] == -1) for i in range(self.winlength)) == self.winlength:
                game_winner = -1;
                game_continue = False;
                return [game_continue,game_winner];
            else:
                game_winner = 0;
                game_continue = True;

            if sum((self.cmap[i,self.winlength-i-1] == 1) for i in range(self.winlength)) == self.winlength:
                game_winner = 1;
                game_continue = False;
                return [game_continue,game_winner];
            elif sum((self.cmap[i,self.winlength-i-1] == -1) for i in range(self.winlength)) == self.winlength:
                game_winner = -1;
                game_continue = False;
                return [game_continue,game_winner];
            else:
                game_winner = 0;
                game_continue = True;

        else:
            game_winner = 0;
            game_continue = False;
            return [game_continue,game_winner];

        return [game_continue,game_winner];

    def game_result(self,winner):
        print("winner: %d"%(winner));
        if winner == 0:
            winner_name = '';
        elif winner == 1:
            winner_name = self.player1_combox.currentText();
        elif winner == -1:
            winner_name = self.player2_combox.currentText();

        showresult = ResultMessage(winner,winner_name);
        showresult.exec_();


class Lattice:
    def __init__(self,x,y,boardhandle):
        super().__init__();
        self.initLattice(x,y,boardhandle);

    def initLattice(self,x,y,boardhandle):
        self.coor = [x,y];
        self.lbutton = QPushButton('',boardhandle);
        self.lbutton.clicked.connect(lambda:self.clicked(boardhandle));
        self.value = 0;
        self.currenthand = True;

    def setGeometry(self,x,y,w,h):
        self.lbutton.setGeometry(x,y,w,h);
        self.lbutton.setVisible(True);

    def setText(self,string):
        self.lbutton.setText(string);

    def clicked(self,boardhandle):
        if self.currenthand:
            self.value = 1;
            self.setText('x');
        else:
            self.value = -1;
            self.setText('o');

        boardhandle.cmap[self.coor[1],self.coor[0]] = self.value;

        for lattice in boardhandle.lattice_list:
            lattice.setHand();

        self.lbutton.setEnabled(False);

        [game_continue,game_winner] = boardhandle.statuscheck();
        print("continue: %s, winner: %d"%(game_continue,game_winner));
        if game_continue:
            boardhandle.mapchanged(True);
        else:
            for lattice in boardhandle.lattice_list:
                lattice.setEnabled(False);
            boardhandle.game_result(game_winner);

    def AImove(self,boardhandle):
        if self.currenthand:
            self.value = 1;
            self.setText('x');
        else:
            self.value = -1;
            self.setText('o');

        boardhandle.cmap[self.coor[1],self.coor[0]] = self.value;

        for lattice in boardhandle.lattice_list:
            lattice.setHand();

        self.lbutton.setEnabled(False);

        [game_continue,game_winner] = boardhandle.statuscheck();
        print("continue: %s, winner: %d"%(game_continue,game_winner));
        if bool(1-game_continue):
            for lattice in boardhandle.lattice_list:
                lattice.setEnabled(False);
            boardhandle.game_result(game_winner);
        else:
            boardhandle.mapchanged(False);
            

    def setHand(self):
        self.currenthand = bool(1-self.currenthand);

    def setEnabled(self,boolflag):
        self.lbutton.setEnabled(boolflag);


class ResultMessage(QDialog):
    def __init__(self,winner,name):
        super().__init__();
        self.game_over(winner,name);

    def game_over(self,winner,name):
        self.setGeometry(500,500,400,300);
        self.setWindowTitle('Game Over!');

        self.message = '';
        if winner == 1:
            self.message = '玩家x：'+name+' 获胜！';
        elif winner == -1:
            self.message = '玩家o：'+name+' 获胜！';
        elif winner == 0:
            self.message = '平局！';

        self.result_label = QLabel(self.message,self);
        self.result_label.setGeometry(100,50,200,50);
        self.result_label.setVisible(True);

        self.Yes_button = QPushButton('确定 重设棋局',self);
        self.Yes_button.setGeometry(150,120,100,30);
        self.Yes_button.setVisible(True);
        self.Yes_button.clicked.connect(lambda:self.closemessage());

    def closemessage(self):
        self.close();


        

if __name__ == "__main__":
    app = QApplication(sys.argv);
    tttv = TTToeView();
    sys.exit(app.exec_());
