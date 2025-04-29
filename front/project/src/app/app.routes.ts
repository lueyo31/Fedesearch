import { Routes } from '@angular/router';
import { InicioComponent } from './components/inicio/inicio.component';
import { ResultsComponent } from './components/results/results.component';
import { ConfigComponent } from './components/config/config.component';

export const routes: Routes = [
  { path: '', component: InicioComponent },
  { path: 'search', component: ResultsComponent },
  { path: 'config', component: ConfigComponent },
  { path: '**', redirectTo: '' },
];
