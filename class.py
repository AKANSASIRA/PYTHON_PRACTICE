class Team:
    def__init_(self,name,Stadium,Capacity,NetWorth,Years,NickName,logo,Legends,Players,MostValuedPlayers,WorldRecords,CurrentCoach,Colour,PremierLeagueTrophies,FATrophies,ChampionsLeagueAppearances):
        self.name=name
        self.Stadium=Stadium
        self.Capacity=Capacity
        self.NetWorth=NetWorth
        self.Years=Years
        self.NickName=NickName
        self.logo=logo
        self.Legends=Legends
        self.Players=Players
        self.MostValuedPlayers=MostValuedPlayers
        self.WorldRecords=WorldRecords
        self.CurrentCoach=CurrentCoach
        self.Colour=Colour
        self.PremierLeagueTrophies=PremierLeagueTrophies
        self.FATrophies=FATrophies
        self.ChampionsLeagueAppearances=ChampionsLeagueAppearances

        def details(self):
            print(self.MostValuedPlayers + "is the most valued" + self.name + "valued player")

            Arsenal=Team("Arsenal", "EmiratesStadium", "2Million", "90BillionUsDollars", "120years+", "TheGunners", "GUN", "TieryHenry,VanPerse,Aubomeyang,SANCHEZ,Songo...", "saka,ramsdale,party,martinelli,ordegard(captain)", "Martinelli","UNBEATEN..GOLDENpremier","ARTETA", "red", "13", "14","131")
            Arsenal.details()