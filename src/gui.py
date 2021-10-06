from os import name, system
import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Space App")
root.resizable(0, 0)
root.geometry("699x600")
root.configure(bg='#fbf1c7')

from image import startingimage, startingimage2, nextimage, previmage, quitimage, astra, northstartbutton, Ruun

def startIspressed():  # THE first button
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    l0 = Label(
        root,
        text="Astranauts life in space",
        font=("Cascadia Code", 24, "bold"),
        foreground="#cc241d",
        background="#fbf1c7",

    )
    lbody = Label(
        root,
        font=("Cascadia Code", 14, "italic"),
        text="Astranauts live a hard life in space. \n The human body  is no designed to live  \nwithout gravity for long periods. \n Thus they face many issues sych as peeling of \nof skin as there is no gravity \nfor the dead cells to fall off.\nDuring their stay on the International Space Station (ISS)\n astronauts have to continue living and working \n in an environment that is very different \n to that here on Earth. They still need to keep clean, \ngo to the bathroom, eat and drink \nand keep fit and healthy. \n The conditions of weightlessness on the ISS mean they need to \n adapt these activities.",
        bg="#fbf1c7"

    )
    l0.pack(pady=(20, 30))
    lbody.pack(pady=(29, 40))

    def destroy():  # The second button
        l0.destroy()
        lbody.destroy()
        nextis.destroy()
        aalboutvenushed = Label(
            root,
            text="Venus",
            font=("Cascadia Code", 24, "bold"),
            fg="#9d0006",
            background="#fbf1c7",

        )
        aalboutvenushed.pack()
        allaboutvenusshedbody = Label(
            root,
            font=("Cascadia Code", 14, "italic"),
            bg="#fbf1c7",
            text="Venus looks like a very active planet.\nVenus is unusual because it spins the opposite direction \n of Earth and most other planets.\n   Because it's so close to the Sun, a year goes by fast. \n It takes 224 Earth days for\n  Venus to go all the way around the Sun. \n That means that a day on Venus is a\n  little longer than a year on Earth.Venus, the Sun \n rises every 117 Earth days. That means the Sun \n rises two times during each \n year on VenusJust like Mercury, Venus doesn't have\n  any moons.",
        )
        allaboutvenusshedbody.pack(pady=(54, 40))

        def IDontWantToDoTHisAgain():  # 2rd button
            allaboutvenusshedbody.destroy()
            aalboutvenushed.destroy()
            Venuskill.destroy()

            astranautsqurantinedtitle = Label(
                root,
                text="After the Appolo Crew visited the Moon",
                font=("Cascadia Code", 19, "bold"),
                bg="#fbf1c7",
                fg="#9d0006",

            )
            # TODO add pictures
            astranautsqurantinedtitle.pack(pady=(15, 30))
            astranautsqurantined = Label(
                root,
                text="Apollo 10 splashed down 920 miles\n southwest of Hawaii and 13 miles \n(21 km) from the USS Hornet, \n a Navy ship sent to recover the crew. The astronauts \nwere trapped inside a NASA trailer as \npart of a quarantine effort just in case \nthey brought back any germs or \ndiseases from the moon.\n They even wore special biological containment \nsuits when they walked out on the deck of the \nUSS Hornet after being retrieved.",
                font=("Cascadia Code", 14, "italic"),
                bg="#fbf1c7"
            )
            astranautsqurantined.pack(pady=(49, 20))

            def NextofAppolo():
                astranautsqurantined.destroy()
                astranautsqurantinedtitle.destroy()
                AstraNautButtonNext.destroy()
                sunhead = Label(
                    root,
                    text="The Sun",
                    bg="#fbf1c7",
                    font=("Cascadia Code", 19, "bold"),
                    fg="#9d0006",
                    border=-1,
                    borderwidth=-1,
                )
                sunhead.pack()

                sunbody = Label(
                    root,
                    text="The Sun. Our Sun \nThe heart of our solar system \n Is a yellow dwarf star, a hot ball of glowing gases\n. Its gravity holds the \nsolar system together\n Keeping everything from the biggest \nplanets to the smallest \nparticles of debris in its orbit \nThe Sun is the largest object in our solar system,\n comprising 99.8% of the solar system’s mass",
                    font=("Cascadia Code", 14, "italic"),
                    border=-1,
                    borderwidth=-1,
                    bg="#fbf1c7"
                )
                sunbody.pack(pady=(50))

                def NorthStar():
                    sunbody.destroy()
                    sunhead.destroy()
                    SunButton.destroy()
                    northstarttitle = Label(
                        text="The North Star",
                        font=("Cascadia Code", 20, "bold"),
                        fg="#9d0006",
                        bg="#fbf1c7",

                    )
                    northstarttitle.pack(pady=(50))

                    nortstarbody = Label(
                        root,
                        text="The North Star is Polaris, \nlocated in the constellation Ursa Minor.\n It does not sit directly on the \nEarth’s north celestial pole,\n but it is very close. In the northern hemisphere, \nPolaris is easy to identify using the \nLittle Dipper as a reference\n. It is Also said that the position \n of North start might change in the \nNear Fututure",
                        font=("Cascadia Code", 14, "italic"),
                        bg="#fbf1c7"
                    )

                    def QuizDecision():
                        nortstarbody.destroy()
                        northstarttitle.destroy()
                        Nect.destroy()
                        Nect.destroy()
                        helpme = Label(
                            root,
                            text="Now run the Quiz.py \n to get the start the quiz or \nclick run to do it automatically\n This window will close and \nstart the quiz if \n you click run .Otherwise click on quit \n to end the app, \nThis app is written in Python ",
                            font=("Cascadia Code", 20, "bold"),
                            fg="#9d0006",
                            bg="#fbf1c7",


                        )
                        About = Label(
                            root,
                            text="This project was developed by Sreehari and Ahil, \n Who are students of SSRVM Banglore East. \n To check out more  projects \n Visit https://github.com/pynvimdev",
                            font=("Jetbrains Mono NF ", 20),
                            bg="#fbf1c7"
                        )
                        About.pack(pady=(20, 40))

                        def Run():
                            if name == "nt":
                                root.destroy()
                                _ = system('python.exe main.py')
                                run.destroy()
                                helpme.destroy()

                            else:
                                root.destroy()
                                _ = system('python3 main.py')
                                run.destroy()
                                helpme.destroy()
                                

                        helpme.pack()

                        run = Button(
                            root,
                            border=-1,
                            image = Ruun, 
                            borderwidth=-1,
                            command=Run
                        )
                        run.pack(pady=(50, 9))

                    Nect = Button(
                        root,
                        borderwidth=-1,
                        border=-1,
                        image = nextimage,
                        font=("Cascadia Code", 14, "bold"),
                        command=QuizDecision,
                    )
                    nortstarbody.pack(pady=(10, 10))

                    Nect.pack(pady=(40))
                SunButton = Button(

                    root,
                    text="Next",
                    border=-1,
                    borderwidth=-1,
                    font=("Cascadia Code", 14, "bold"),
                    image=nextimage,
                    command=NorthStar,
                )
                SunButton.pack(pady=(30, 40))

            AstraNautButtonNext = Button(
                root,
                text="Next",
                font=("Cascadia Code", 14, "bold"),
                border=-1,
                image=nextimage,
                borderwidth=-1,
                command=NextofAppolo

            )
            AstraNautButtonNext.pack(pady=40)

        Venuskill = Button(
            root,
            image=nextimage,
            border=-1,
            borderwidth=-1,
            height=85,
            command=IDontWantToDoTHisAgain,
        )
        Venuskill.pack(pady=(2, 5))
    nextis = Button(
        root,
        font=("Cascadia Code", 14),
        border=-1,
        image=astra,
        command=destroy
    )
    nextis.pack(pady=(1, 10))


labelimage = Label(
    root,
    image=startingimage,
    background="#ffffff",
)
labelimage.pack(pady=(39, 0))

labeltext = Label(
    root,
    text="Space App",
    font=("Comic sans MS", 23, "bold"),
    background="#fbf1c7",
)
labeltext.pack(pady=(1, 50))


btnStart = Button(
    root,
    image=startingimage2,
    relief=FLAT,
    text="Start",
    width=140,
    height=70,
    border=-1,
    borderwidth=-1,
    command=startIspressed,
)
btnStart.pack(pady=(10, 10))

lblInstruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are ready",
    background="#fbf1c7",
    font=("Jetbrains Mono NF ", 13),
    justify="center",
)

lblInstruction.pack(pady=(9, 100))

lblRules = Label(
    root,
    text="This app will educate you about some amazing facts about space First \nYou will be given information and then the \n QUIZ will be taken which comprises of 21 questions\n Note: Extra questions will be asked in the quiz",
    height=130,
    width=120,
    font=("Times", 13),
    background="#928174",
    foreground="#000000",
)
lblRules.pack()
root.mainloop()
