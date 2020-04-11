import { Component, OnInit } from '@angular/core';
import { Game } from 'src/app/models/game';
import { Player } from 'src/app/models/player';
import { GameFinderService } from 'src/app/services/game-finder.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-ongoing-games',
  templateUrl: './ongoing-games.component.html',
  providers: [GameFinderService],
  styleUrls: ['./ongoing-games.component.scss']
})
export class OngoingGamesComponent implements OnInit {

  public games: Array<Game>

  constructor(private _gameFinderService: GameFinderService, private router: Router) { }

  ngOnInit(): void {
    this.games = new Array<Game>()
    const game1 = new Game("Cyril's party", "Briscola", 4);
    const game2 = new Game("Maghi's party", "Briscola", 3);
    game2.players.push(new Player())
    this.games.push(game1)
    this.games.push(game2)
  }

  enterGame(game: Game) {
    let gameToEnter = this._gameFinderService.getGame(game.uuid)
    this.router.navigate(['Briscola', gameToEnter])
  }

}
