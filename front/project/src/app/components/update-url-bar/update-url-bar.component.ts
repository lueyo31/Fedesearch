import { Component, OnDestroy } from '@angular/core';
import { ConfigService } from '../../services/config/config.service';
import { FormsModule } from '@angular/forms';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-update-url-bar',
  imports: [FormsModule],
  templateUrl: './update-url-bar.component.html',
  styleUrl: './update-url-bar.component.scss'
})
export class UpdateUrlBarComponent implements OnDestroy {
  currentUrl: string = '';
  inputValue: string = '';
  urlUpdated: boolean = false;
  private subscriptions: Subscription = new Subscription();

  constructor(private configService: ConfigService) {
    this.configService.getApiUrl().subscribe((url) => {
      console.log('API URL updated in UpdateUrlBarComponent:', url);
      this.currentUrl = url; // Update the current URL dynamically
    });
  }

  ngOnInit() {
    this.subscriptions.add(
      this.configService.getApiUrl().subscribe((url) => {
        console.log('Current URL:', url);
        this.currentUrl = url;
      })
    );
  }

  ngOnDestroy() {
    this.subscriptions.unsubscribe();
  }

  updateUrl() {
    this.configService.updateApiUrl(this.inputValue);
    this.configService.getApiUrl().subscribe((url) => {
      console.log('Updated URL:', url);

      this.currentUrl = url;
      this.urlUpdated = true;
      setTimeout(() => {
        this.urlUpdated = false;
      }
        , 3000); // Hide the message after 3 seconds
    });
  }
}
