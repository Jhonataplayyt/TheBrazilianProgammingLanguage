a = 1664525

c = 1013904223

m = 2^32



seed = 1234567890



min = 0



max = 3



ic = 0

ibc = 0



println("jogo:\n    Pedra, Papel e Tesoura")

println("        1.Pedra\n        2.Papel\n        3.Tesoura")



while true then

    if ic >= 3 then

        println("Você Ganhou! de: \n    " + str(ic) + "x" + str(ibc))

        

        break

     elif ibc >= 3 then

          println("Você Perdeu! de: \n    " + str(ibc) + "x" + str(ic))

          

          break

     end



    seed = (a * seed + c) % m



    seed = min + (seed % (max - min + 1))



    ib = seed



    print("\n        Você: ")

    i = input("")



    if i == "cls" then

        clear()

        

        println("jogo:\n    Pedra, Papel e Tesoura")

        println("        1.Pedra\n        2.Papel\n        3.Tesoura")

    elif i == "1" or i == "2" or i == "3" then

        i = int(i)



        if i <= 3 then

            if ib == 1 then

                println("    Bot:\n              Pedra")

            elif ib == 2 then

                println("    Bot:\n              Papel")

            else

                println("    Bot: \n              Tesoura")

            end



            if i == 1 and ib == 3 then

                println("Você Ganhou")

                

                ic = ic + 1

            elif i == 1 and ib == 2 then

                println("Você Perdeu")

                

                ibc = ibc + 1

            elif i == 2 and ib == 1 then

                println("Você Ganhou")

                

                ic = ic + 1

            elif i == 2 and ib == 3 then

                println("Você Perdeu")

                

                ibc = ibc + 1

            elif i == 3 and ib == 2 then

                println("Você Ganhou")

                

                ic = ic + 1

            elif i == 3 and ib == 1 then

                println("Você Perdeu")

                

                ibc = ibc + 1

            else

                println("Empatou")

            end

        else

            println("Você precisa colocar 1, 2 ou 3 para jogar e não '" + str(i) + "'")

        end

    else

        println("Você precisa colocar 1, 2 ou 3 para jogar e não '" + str(i) + "'")

    end

end
