using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace game
{
    public class Player : Mob
    {
        public Inventory inventory;

        public bool hasYrden;
        public int yrdenDamage;
        public int quenTurns;
        public int choice;
        public int orioleTime;
        public int currentAttackType; // 0 - none, 1 - swords, 2 - signs, 3 - inventory
        public Position position;
        public Player()
        {
            //Console.WriteLine("Called constructor from Player");
            this.position = new Position(0, 53, 7);
            this.inventory = new Inventory();
            this.Name = "Gerwazy";
            this.maxHP = 500;
            this.maxMana = 250;
            this.hasYrden = false;
            this.yrdenDamage = 0;
            this.quenTurns = 0;
            this.orioleTime = 0;
           
            //Stuff for combat
            this.choice = 0;
            this.currentAttackType = 0;

            this.inventory.Add("Swallow");
            this.inventory.Add("Golden Oriole");

            Mob.initialiseMob(this);
        }


        public void Igni(Mob target) // sets an enemy on fire for 2 turn making damage at the beginning of every turn
        {
            target.onFire = 3;

            Damage fireDamage = new Damage();
            fireDamage.damage["fire"] = 20;

            this.DealDamage(target, fireDamage);
            if (this.currentMana >= 30)
            {
                currentMana -= 30;
            }
        }
        public void Aard(Mob target) // stuns an enemy for two turns
        {
            target.stunned += 2;
            if (this.currentMana >= 15)
            {
                currentMana -= 15;
            }
        }
        public void Yrden() // enemy attacking the player with yrden takes magic damage
        {
            this.hasYrden = true;
            this.yrdenDamage = 30;
            if(this.currentMana >= 20)
            {
                currentMana -= 20;
            }
        }
        public void Quen() // decreases witcher's valnurability (for 2 turns)
        {
            this.valnurabilities["slash"] = 0.5;
            this.quenTurns = 2;
            if (this.currentMana >= 15)
            {
                currentMana -= 15;
            }
        }
        public void PickUp(Item item)
        {
            
        }

        public void MoveUp()
        {
            if(Map.mapArray[this.position.room, this.position.y - 1, this.position.x] != 1)
            {
                this.position.y -= 1;
            }
        }
        public void MoveDown()
        {
            if (Map.mapArray[this.position.room, this.position.y + 1, this.position.x] != 1)
            {
                this.position.y += 1;
            }
        }
        public void MoveLeft()
        {
            if (Map.mapArray[this.position.room, this.position.y, this.position.x - 1] != 1)
            {
                this.position.x -= 1;
            }
        }
        public void MoveRight()
        {
            if (Map.mapArray[this.position.room, this.position.y, this.position.x + 1] != 1)
            {
                this.position.x += 1;
            }
        }

        public void PreviousChoice()
        {
            if(this.currentAttackType == 0)
            {
                if(this.choice > 1)
                {
                    this.choice--;
                }
            } 
            else if(this.currentAttackType == 1)
            {
                if (this.choice > 1)
                {
                    this.choice--;
                }
            } 
            else if(this.currentAttackType == 2)
            {
                if (this.choice > 1)
                {
                    this.choice--;
                }
            }
            else if(this.currentAttackType == 3)
            {
                if (this.choice > 1)
                {
                    this.choice--;
                }
            }
        }
        public void NextChoice()
        {
            if (this.currentAttackType == 0)
            {
                if(this.choice < 3)
                {
                    this.choice++;
                }
            }
            else if (this.currentAttackType == 1)
            {
                if (this.choice < 3)
                {
                    this.choice++;
                }
            }
            else if (this.currentAttackType == 2)
            {
                if (this.choice < 5)
                {
                    this.choice++;
                }
            }
            else if (this.currentAttackType == 3)
            {
                if (this.choice < this.inventory.items.Count + 1)
                {
                    this.choice++;
                }
            }
        }
        public int Select() //0 for nothing chosen, 1 for targetless, 2 for steel, 3 for silver, 4 - aard, 5 - igni
        {
            Console.WriteLine("Select() called");
            if(this.currentAttackType == 0)
            {
                if(this.choice == 1) 
                {
                    this.currentAttackType = 1;
                    this.choice = 1;
                    return 0;
                } 
                else if (this.choice == 2)
                {
                    this.currentAttackType = 2;
                    this.choice = 1;
                    return 0;
                }
                else if (this.choice == 3)
                {
                    this.currentAttackType = 3;
                    this.choice = 1;
                    return 0;
                }
            }
            else if(this.currentAttackType == 1) //swords
            {
                if(this.choice == 1)
                {
                    this.currentAttackType = 0;
                    this.choice = 1;
                    return 0;
                } else if(this.choice == 2)
                {
                    return 2;
                } else if (this.choice == 3)
                {
                    return 3;
                }
            } 
            else if(this.currentAttackType == 2) //signs
            {
                if (this.choice == 1) //back
                {
                    this.currentAttackType = 0;
                    this.choice = 1;
                    return 0;
                } else if(this.choice == 2) //aard
                {
                    this.currentAttackType = 0;
                    this.choice = 1;
                    return 4;
                } else if(this.choice == 3) //igni
                {
                    this.currentAttackType = 0;
                    this.choice = 1;
                    return 5;
                } else if( this.choice == 4) //yrden
                {
                    this.currentAttackType = 0;
                    this.choice = 1;
                    Yrden();
                    return 1;
                } else if(this.choice == 5) //quen
                {
                    this.currentAttackType = 0;
                    this.choice = 1;
                    Quen();
                    return 1;
                }
            } 
            else if(this.currentAttackType == 3) //inventory
            {
                if (this.choice == 1)
                {
                    this.currentAttackType = 0;
                    this.choice = 1;
                    return 0;
                } else
                {
                    Console.WriteLine("{0} dupa", this.inventory.items[choice - 2].Name);
                    UsePotion();
                    return 1;
                    
                }
            }
            return 0;
        }
        public void UsePotion()
        {
            //Console.WriteLine("UsePotion() called");
            if(this.inventory.items[choice - 2].Name == "Swallow")
            {
                this.currentHP += 150;
                if(this.currentHP > this.maxHP)
                    this.currentHP = this.maxHP;

                this.inventory.items.RemoveAt(choice - 2);
                return;
            } 
            else if (this.inventory.items[choice - 2].Name == "Tawny Owl")
            {
                this.currentMana += 100;
                if(this.currentMana > this.maxMana)
                    this.currentMana = this.maxMana;

                this.inventory.items.RemoveAt(choice - 2);
                return;
            } 
            else if (this.inventory.items[choice - 2].Name == "Golden Oriole")
            {
                this.poisoned = 0;
                this.valnurabilities["poison"] = 0.0;
                this.orioleTime = 5;

                this.inventory.items.RemoveAt(choice - 2);
                return;
            } 
        }
    }
}
