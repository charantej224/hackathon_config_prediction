import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BsDatepickerModule } from 'ngx-bootstrap/datepicker';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { AmazingTimePickerModule } from 'amazing-time-picker';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { GraphsComponent } from './graphs/graphs.component';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';
import { ChartsModule } from 'ng2-charts';
import { ConfigrequestComponent } from './configrequest/configrequest.component';

const appRoutes: Routes = [
    { path: '', component: HomeComponent, canActivate: [AuthGuard] },
    { path: 'graphs', component: GraphsComponent, canActivate: [AuthGuard] }
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    GraphsComponent,
    ConfigrequestComponent
  ],
  imports: [
    BrowserModule,
      FormsModule,
      AmazingTimePickerModule,
      BsDatepickerModule.forRoot(),
      BrowserAnimationsModule,
      HttpClientModule,
      RouterModule.forRoot(appRoutes),
      ChartsModule
  ],
    providers: [AuthGuard],
    bootstrap: [AppComponent]
})
export class AppModule { }
