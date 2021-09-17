
from os import name, system
import tkinter
from tkinter import *
from tkinter import font

root = tkinter.Tk()
root.title("Space App")
root.geometry("699x600")
root.config(background="#ffffff")
root.configure(bg='#ffffff')
img0 = PhotoImage(file="transparentGradHat.png")
img1 = PhotoImage(file="Frame.png")


def startIspressed():# THE first button
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    l0 = Label(
        root,
        text = "Astranauts life in space",
        font = ("Cascadia Code",19,"bold"),
        foreground = "#ADD7E6",
        background = "#ffffff",

    )
    lbody = Label(
        root,
        font = ("Cascadia Code",14,"italic"),
        text = "Astranauts live a hard life in space. \n The human body  is no designed to live  \nwithout gravity for long periods. \n Thus they face many issues sych as peeling of \nof skin as there is no gravity \nfor the dead cells to fall off.\nDuring their stay on the International Space Station (ISS)\n astronauts have to continue living and working \n in an environment that is very different \n to that here on Earth. They still need to keep clean, \ngo to the bathroom, eat and drink \nand keep fit and healthy. \n The conditions of weightlessness on the ISS mean they need to \n adapt these activities.",
        bg = "#ffffff"

    )
    l0.pack(pady=(20,30))
    lbody.pack(pady =(29,40) )

    # TODO understand this properly
    def destroy():# The second button
        l0.destroy()
        lbody.destroy()
        nextis.destroy()
        aalboutvenushed = Label(
            root,
            text = "Venus",
            font = ("Cascadia Code",19,"bold"),
            foreground = "#ADD7E6",
            background = "#ffffff",

        )
        aalboutvenushed.pack()
        allaboutvenusshedbody = Label(
            root,
            font = ("Cascadia Code",14,"italic"),
            bg = "#ffffff",
            text = "Venus looks like a very active planet.\nVenus is unusual because it spins the opposite direction \n of Earth and most other planets.\n   Because it's so close to the Sun, a year goes by fast. \n It takes 224 Earth days for\n  Venus to go all the way around the Sun. \n That means that a day on Venus is a\n  little longer than a year on Earth.Venus, the Sun \n rises every 117 Earth days. That means the Sun \n rises two times during each \n year on VenusJust like Mercury, Venus doesn't have\n  any moons.",
        )
        allaboutvenusshedbody.pack(pady=(54,40))
        def IDontWantToDoTHisAgain():# 2rd button
            allaboutvenusshedbody.destroy()
            aalboutvenushed.destroy()
            Venuskill.destroy()

            astranautsqurantinedtitle = Label(
                root,
                text = "After the Appolo Crew visited the Moon",
                font = ("Cascadia Code",19,"bold"),
                bg = "#ffffff",
                fg = "#ADD7E6",

            )
            # TODO add pictures
            astranautsqurantinedtitle.pack()
            astranautsqurantined = Label(
                root,
                text = "Apollo 10 splashed down 920 miles\n southwest of Hawaii and 13 miles \n(21 km) from the USS Hornet, \n a Navy ship sent to recover the crew. The astronauts \nwere trapped inside a NASA trailer as \npart of a quarantine effort just in case \nthey brought back any germs or \ndiseases from the moon.\n They even wore special biological containment \nsuits when they walked out on the deck of the \nUSS Hornet after being retrieved.",
                font = ("Cascadia Code",14,"italic"),
                bg = "#ffffff"
            )
            astranautsqurantined.pack(pady=(49,20))
            
            def NextofAppolo():
                astranautsqurantined.destroy()
                astranautsqurantinedtitle.destroy()
                nexter.destroy()
                sunhead = Label(
                    root,
                    text = "The Sun",
                    bg = "#ffffff",
                    font = ("Cascadia Code",19,"bold"),
                    fg = "#ADD7E6",
                    border= -1,
                    borderwidth= -1,
                )
                sunhead.pack()

                sunbody = Label(
                    root,
                    text = "The Sun. Our Sun \nThe heart of our solar system \n Is a yellow dwarf star, a hot ball of glowing gases\n. Its gravity holds the \nsolar system together\n Keeping everything from the biggest \nplanets to the smallest \nparticles of debris in its orbit \nThe Sun is the largest object in our solar system,\n comprising 99.8% of the solar system’s mass",
                    font = ("Cascadia Code",14,"italic"),
                    border = -1,
                    borderwidth = -1,
                    bg = "#ffffff"
                )
                sunbody.pack(pady=(50))

                def NorthStar():
                    sunbody.destroy()
                    sunhead.destroy()
                    NextForTheQuiz.destroy()
                    northstarttitle = Label(
                        text = "The North Star",
                        font = ("Cascadia Code",20,"bold"),
                        fg = "#ADD7E6",
                        bg = "#ffffff",
                        
                    )
                    northstarttitle.pack(pady=(50))

                    nortstarbody = Label(
                        root,
                        text = "The North Star is Polaris, \nlocated in the constellation Ursa Minor.\n It does not sit directly on the \nEarth’s north celestial pole,\n but it is very close. In the northern hemisphere, \nPolaris is easy to identify using the \nLittle Dipper as a reference\n. It is Also said that the position \n of North start might change in the \nNear Fututure",
                        font = ("Cascadia Code",14,"italic"),
                        bg = "#ffffff"
                    )
                    def QuizDecision():
                        nortstarbody.destroy()
                        northstarttitle.destroy()
                        NextForTheQuiz.destroy()
                        Nect.destroy()
                        helpme = Label(
                            root,
                            text = "Now run the Quiz.py \n to get the start the quiz or \nclick run to do it automatically",
                            font = ("Cascadia Code",20,"bold"),
                            fg = "#ADD7E6",
                            bg = "#ffffff",


                        )
                        def Run():
                            if name == "nt":
                                _ = system('python main.py')
                                run.destroy()
                                helpme.destroy()
                                helping = Label(
                                    root,
                                    text = "Started running ....",
                                    font = ("Cascadia Code",13,"bold"),
                                    bg = "#ffffff"
                                )
                                helping.pack()

                            else:
                                print("unsopported")
                                exit()
                        
                        helpme.pack()

                        run = Button(
                            root,
                            text = "Run",
                            background = "#008000",
                            border = -1,
                            width = 5,
                            height = 2,
                            font = ("Cascadia Code",15,"bold"),
                            borderwidth = -1,  
                            command = Run
                        )
                        run.pack(pady=(20))

                        def About():
                            helpme.destroy()
                            run.destroy()
                            Author.destroy()
                            Labeld = Label(
                                root,
                                text = "This project is Made by Ahil and \nSreehari of Class-8b,\n And is made with Python. \nIt requires git and python \ninstalled \n to run on local machine\n Thank You \n. Want to contribute ? \n Check my github: \n Sreehariqwerty(username)",
                                bg = "#ffffff",
                                font = ("Cascadia Code",14,"bold")
                            )
                            Labeld.pack()
                        Author = Button(
                            root,
                            text = "About",
                            command = About,
                            height = 2,
                            border = -1,
                            borderwidth = -1,
                            width = 7,
                            font = ("Cascadia Code",17,"bold"),
                            bg = "#ADD7E6",
                        )
                        Author.pack(pady=(30))
                    Nect = Button(
                        root,
                        text = "Next",
                        bg = "#ADD7E6",
                        borderwidth = -1,
                        border = -1,
                        font = ("Cascadia Code",14,"bold"),
                        command = QuizDecision, 
                    )
                    nortstarbody.pack()
                    Nect.pack(pady=(40))
                NextForTheQuiz = Button(
                        root,
                        text = "Next",
                        border = -1,
                        borderwidth = -1,
                        bg = "#ADD7E6",
                        font = ("Cascadia Code",14,"bold"),
                        command = NorthStar,
                )
                NextForTheQuiz.pack()



            nexter = Button(
                root,
                text = "Next",
                font = ("Cascadia Code",14,"bold"),
                bg = "#ADD7E6",
                border=-1,
                borderwidth=-1,
                command = NextofAppolo

            )
            nexter.pack(pady=29)


        Venuskill = Button(
            root,
            text = "Next",
            font = ("Cascadia Code",14,"bold"),
            bg = "#ADD7E6",
            border = -1,
            borderwidth = -1, 
            command = IDontWantToDoTHisAgain,
        )
        Venuskill.pack()
    # TODO add pctures
    nextis = Button(
        root,
        font = ("Cascadia Code",14),
        border = -1,
        bg = "#ADD7E6",
        text = "Next",
        command = destroy
    )
    nextis.pack()


labelimage = Label(
    root,
    image = img0,
    background = "#ffffff",
)
labelimage.pack(pady=(39,0))

labeltext = Label(
    root,
    text = "Space App",
    font = ("Comic sans MS",23,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(1,50))


btnStart = Button(
    root,
    image = img1,
    relief = FLAT,
    text = "Start",
    border = -1,
    borderwidth = -1,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",13),
    justify = "center",
)

lblInstruction.pack(pady=(9,100))

lblRules = Label(
    root,
    text = "This app will educate you about some amazing facts about space First \nYou will be given information and then the \n QUIZ will be taken which comprises of 21 questions\n Note: Extra questions will be asked in the quiz",
    height=100,
    width = 99,
    font = ("Times",13),
    background = "#ADD7E6",
    foreground = "#000000",
)
lblRules.pack()

root.mainloop()