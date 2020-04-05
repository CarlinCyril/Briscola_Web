import { Component, OnInit } from '@angular/core';
import { Card } from '../../models/card';

@Component({
  selector: 'app-table-game',
  templateUrl: './table-game.component.html',
  styleUrls: ['./table-game.component.scss']
})
export class TableGameComponent implements OnInit {

  public listPlayerCards: Array<Card>;
  public southPlayerCard: Card;
  public northPlayerCard: Card;
  public eastPlayerCard: Card;
  public westPlayerCard: Card;

  constructor() { }

  ngOnInit() {
    this.listPlayerCards = this.getPlayerCards();
  }

  clickedCard(card: Card) {
    this.southPlayerCard = card;
    this.listPlayerCards.splice(this.listPlayerCards.indexOf(card), 1);
  }


  /**
* Temporary list of cards.
*/
  public getPlayerCards(): Array<Card> {
    let playerCards = new Array<Card>();
    playerCards.push(new Card("2", "D"));
    playerCards.push(new Card("3", "S"));
    playerCards.push(new Card("4", "C"));
    playerCards.push(new Card("5", "H"));
    playerCards.push(new Card("6", "D"));
    return playerCards.sort((x, y) => x.compare(y));
  }

}
