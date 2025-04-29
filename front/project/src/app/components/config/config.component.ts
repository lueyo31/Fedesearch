import { Component, OnDestroy } from '@angular/core';
import { ConfigService } from '../../services/config/config.service';
import { userConfig } from '../../models/configParams';
import { FormsModule } from '@angular/forms';
import { UpdateUrlBarComponent } from '../update-url-bar/update-url-bar.component';
import { Language } from '../../models/language';
import { RouterLink } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-config',
  imports: [FormsModule, UpdateUrlBarComponent, RouterLink],
  templateUrl: './config.component.html',
  styleUrl: './config.component.scss',
})
export class ConfigComponent implements OnDestroy {
  config: userConfig = {};
  languages!: Language[];
  successMessage: string = '';
  errorMessage: string = '';
  private subscriptions: Subscription = new Subscription();

  constructor(private configService: ConfigService) { }

  ngOnInit() {
    this.languages = this.configService.getLanguages();
    this.subscriptions.add(
      this.configService.getCurrentConfig().subscribe((currentConfig) => {
        this.config = { ...this.config, ...currentConfig };
      })
    );
  }

  ngOnDestroy() {
    this.subscriptions.unsubscribe();
  }

  updateConfig(field: keyof userConfig): void {
    const updatedConfig: userConfig = { [field]: this.config[field] };
    this.configService.updateServerConfig(updatedConfig).subscribe(
      () => {
        this.successMessage = 'Cambios guardados correctamente';
        this.errorMessage = '';
        setTimeout(() => {
          this.successMessage = '';
        }, 3000);
      },
      (error) => {
        this.errorMessage = `Error al guardar los cambios: ${error.message}`;
        this.successMessage = '';
        setTimeout(() => {
          this.errorMessage = '';
        }, 3000);
      }
    );
  }
}
