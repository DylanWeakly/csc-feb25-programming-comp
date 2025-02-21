# Johnathan Feter GUI 2

import tkinter as tk
import tkinter.messagebox
import random as rd

class bible_ver:
    def __init__(self):

        self.main_window = tk.Tk()
        self.frame = tk.Frame(self.main_window)
        self.generate_ver = tk.Button(self.frame, text="Generate Bible Verse", command=self.change_button)
        self.generate_ver.pack(side='top')
        self.frame.pack()

        tk.mainloop()

    def change_button(self):
        random_number = rd.randint(1,20)
        message = ''

        if random_number == 1:
            message = ('Philippians 4:7\nAnd the peace of God, which transcends all understanding, will guard your '
                       'hearts and your minds in Christ Jesus.')
        if random_number == 2:
            message = ('Matthew 18:15\nIf your brother or sister sins, go and point out their fault, just between the '
                       'two of you. If they listen to you, you have won them over.')
        if random_number == 3:
            message = ('Mark 11:17\nAnd as he taught them, he said, “Is it not written: ‘My house will be called a '
                       'house of prayer for all nations’? But you have made it ‘a den of robbers.')
        if random_number == 4:
            message = ('Luke 2:22\nWhen the time came for the purification rites required by the Law of Moses, '
                       'Joseph and Mary took him to Jerusalem to present him to the Lord')
        if random_number == 5:
            message = ('John 3:16\nFor God so loved the world that he gave his one and only Son, that whoever believes '
                       'in him shall not perish but have eternal life.')
        if random_number == 6:
            message = ('Acts 18:9-10\nOne night the Lord spoke to Paul in a vision: Do not be afraid; keep on '
                       'speaking, do not be silent.For I am with you, and no one is going to attack and harm you, '
                       'because I have many people in this city.')
        if random_number == 7:
            message = ('Romans 2:12\nAll who sin apart from the law will also perish apart from the law, and all who '
                       'sin under the law will be judged by the law.')
        if random_number == 8:
            message = ('1 Corinthians 8:9\nBe careful, however, that the exercise of your rights does not become a '
                       'stumbling block to the weak.')
        if random_number == 9:
            message = ('2 Corinthians 9:6\nRemember this: Whoever sows sparingly will also reap sparingly, and whoever '
                       'sows generously will also reap generously.')
        if random_number == 10:
            message = ('Galatians 1:6\nI am astonished that you are so quickly deserting the one who called you to '
                       'live in the grace of Christ and are turning to a different gospel')
        if random_number == 11:
            message = ('Ephesians 1:15\nFor this reason, ever since I heard about your faith in the Lord Jesus and '
                       'your love for all God’s people')
        if random_number == 12:
            message = ('Philippians 2:6\nWho, being in very nature God, did not consider equality with God something '
                       'to be used to his own advantage;')
        if random_number == 13:
            message = ('Colossians 3:18-19\nWives, submit yourselves to your husbands, as is fitting in the Lord. '
                       'Husbands, love your wives and do not be harsh with them.')
        if random_number == 14:
            message = ('1 Thessalonians 5:12\nNow we ask you, brothers and sisters, to acknowledge those who work hard '
                       'among you, who care for you in the Lord and who admonish you.')
        if random_number == 15:
            message = ('2 Thessalonians 2:13\nBut we ought always to thank God for you, brothers and sisters loved by '
                       'the Lord, because God chose you as firstfruits to be saved through the sanctifying work of '
                       'the Spirit and through belief in the truth.')
        if random_number == 16:
            message = ('1 Timothy 3:11\nIn the same way, the women are to be worthy of respect, not malicious talkers '
                       'but temperate and trustworthy in everything.')
        if random_number == 17:
            message = ('2 Timothy 2:14\nKeep reminding God’s people of these things. Warn them before God against '
                       'quarreling about words; it is of no value, and only ruins those who listen.')
        if random_number == 18:
            message = ('Titus 1:10\nFor there are many rebellious people, full of meaningless talk and deception, '
                       'especially those of the circumcision group.')
        if random_number == 19:
            message = ('Philemon 1:16\nno longer as a slave, but better than a slave, as a dear brother. He is very '
                       'dear to me but even dearer to you, both as a fellow man and as a brother in the Lord.')
        if random_number == 20:
            message = ('Hebrews 13:6\nSo we say with confidence, The Lord is my helper; I will not be afraid. What can '
                       'mere mortals do to me?')

        tk.messagebox.showinfo('Bible Verse', f'{message}')

if __name__ == '__main__':
    bible_ver()