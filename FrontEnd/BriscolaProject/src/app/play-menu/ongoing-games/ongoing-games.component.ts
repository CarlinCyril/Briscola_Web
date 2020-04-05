import { Component, OnInit } from '@angular/core';
import { Game } from 'src/app/models/game';
import { Player } from 'src/app/models/player';

@Component({
  selector: 'app-ongoing-games',
  templateUrl: './ongoing-games.component.html',
  styleUrls: ['./ongoing-games.component.scss']
})
export class OngoingGamesComponent implements OnInit {

  public games: Array<Game>

  constructor() { }

  ngOnInit(): void {
    this.games = new Array<Game>()
    const game1 = new Game("Cyril's party", "Briscola", 4);
    const game2 = new Game("Maghi's party", "Briscola", 3);
    game2.players.push(new Player())
    this.games.push(game1)
    this.games.push(game2)
  }

}
