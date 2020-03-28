import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './home/navbar/navbar.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { QuickSearchComponent } from './quick-search/quick-search.component';
import { PlayMenuComponent } from './play-menu/play-menu.component';
import { CreateGameComponent } from './play-menu/create-game/create-game.component';
import { OngoingGamesComponent } from './play-menu/ongoing-games/ongoing-games.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavbarComponent,
    NotFoundComponent,
    QuickSearchComponent,
    PlayMenuComponent,
    CreateGameComponent,
    OngoingGamesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    NgbModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
