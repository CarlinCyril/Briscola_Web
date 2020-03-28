import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NotFoundComponent } from './not-found/not-found.component';
import { HomeComponent } from './home/home.component';
import { PlayMenuComponent } from './play-menu/play-menu.component';
import { CreateGameComponent } from './play-menu/create-game/create-game.component';
import { OngoingGamesComponent } from './play-menu/ongoing-games/ongoing-games.component';


const routes: Routes = [
  { path: 'Home', component: HomeComponent },
  { path: 'Play', component: OngoingGamesComponent},
  { path: 'CreateGame', component: CreateGameComponent},
  { path: '', redirectTo: '/Home', pathMatch: 'full' },
  { path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }