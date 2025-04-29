import { Injectable } from '@angular/core';
import { userConfig } from '../../models/configParams';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { Language } from '../../models/language';
import { tap, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class ConfigService {
  constructor(private http: HttpClient) { }
  apiVersion: string = '1';
  apiUrl: BehaviorSubject<string> = new BehaviorSubject<string>(
    localStorage.getItem('apiUrl') || this.getEnvUrl()
  );

  updateApiUrl(newUrl: string): void {
    // añade http:// si la url no empieza por http:// o https://
    if (!newUrl.startsWith('http://') && !newUrl.startsWith('https://')) {
      newUrl = `http://${newUrl}`;
    }

    // comprueba si la url es correcta
    const urlPattern =
      /^(http?:\/\/|https?:\/\/)?((localhost)|((\d{1,3}\.){3}\d{1,3})|([\da-z.-]+))(:[0-9]{1,5})?(\/[\/\w .-]*)*\/?$/;
    if (!urlPattern.test(newUrl)) {
      console.error('Invalid URL format');
      return;
    }

    // comprueba si la url acaba en /
    if (newUrl[newUrl.length - 1] !== '/') {
      newUrl += '/';
    }
    this.pingAbout(newUrl).subscribe(
      (response) => {
        this.apiVersion = response.api_version;
        console.log('Ping successful', response);

        // Update the BehaviorSubject with the new URL
        const updatedUrl = `${newUrl}api/v${this.apiVersion}`;
        this.apiUrl.next(updatedUrl);

        // Store the updated URL in localStorage
        localStorage.setItem('apiUrl', updatedUrl);
      },
      (error) => {
        console.error('Ping failed', error);
        return;
      }
    );
  }

  getApiUrl(): Observable<string> {
    return this.apiUrl.asObservable(); // Return the BehaviorSubject as an Observable
  }
  getApiUrlAsString(): string {
    return this.apiUrl.getValue(); // Get the current value of the BehaviorSubject
  }
  updateServerConfig(params: userConfig): Observable<any> {
    console.log(this.getApiUrlAsString());
    let newConfig = {
      params,
      xng_params: {}, // Include xng_params as an empty object
    };
    return this.http
      .patch(`${this.getApiUrlAsString()}/config`, newConfig)
      .pipe(
        tap((response: any) => {
          console.log('Config updated successfully', response);

          // Update or replace the property in fedeConfig in localStorage
          const fedeConfig = JSON.parse(
            localStorage.getItem('fedeConfig') || '{}'
          );
          Object.assign(fedeConfig, params); // Merge the updated params into fedeConfig
          localStorage.setItem('fedeConfig', JSON.stringify(fedeConfig));
        }),
        catchError((error: any) => {
          console.error('Error updating config', error);
          throw error;
        })
      );
  }
  getCurrentConfig(): Observable<userConfig> {
    return new Observable<userConfig>((observer) => {
      const config = localStorage.getItem('fedeConfig');
      if (config) {
        observer.next(JSON.parse(config));
      } else {
        console.error('Config not found in localStorage');
        observer.next({}); // Return an empty object if no config is found
      }
      observer.complete();
    });
  }

  pingAbout(url: string): Observable<any> {
    return this.http.get<any>(`${url}about`);
  }
  getLanguages(): Language[] {
    return [
      { code: 'en-US', name: 'English, United States' },
      { code: 'en-GB', name: 'English, United Kingdom' },
      { code: 'es-ES', name: 'Spanish, Spain' },
      { code: 'es-MX', name: 'Spanish, Mexico' },
      { code: 'es-PE', name: 'Spanish, Peru' },
      { code: 'fr-FR', name: 'French, France' },
      { code: 'fr-CA', name: 'French, Canada' },
      { code: 'de-DE', name: 'German, Germany' },
      { code: 'it-IT', name: 'Italian, Italy' },
      { code: 'pt-BR', name: 'Portuguese, Brazil' },
      { code: 'pt-PT', name: 'Portuguese, Portugal' },
      { code: 'zh-CN', name: 'Chinese, China (Simplified)' },
      { code: 'zh-TW', name: 'Chinese, Taiwan (Traditional)' },
      { code: 'ja-JP', name: 'Japanese, Japan' },
      { code: 'ko-KR', name: 'Korean, South Korea' },
      { code: 'ar-SA', name: 'Arabic, Saudi Arabia' },
      { code: 'ar-EG', name: 'Arabic, Egypt' },
      { code: 'ru-RU', name: 'Russian, Russia' },
      { code: 'hi-IN', name: 'Hindi, India' },
      { code: 'bn-BD', name: 'Bengali, Bangladesh' },
      { code: 'ms-MY', name: 'Malay, Malaysia' },
      { code: 'sw-KE', name: 'Swahili, Kenya' },
      { code: 'tr-TR', name: 'Turkish, Turkey' },
      { code: 'vi-VN', name: 'Vietnamese, Vietnam' },
      { code: 'th-TH', name: 'Thai, Thailand' },
      { code: 'nl-NL', name: 'Dutch, Netherlands' },
      { code: 'nl-BE', name: 'Dutch, Belgium' },
      { code: 'pl-PL', name: 'Polish, Poland' },
      { code: 'sv-SE', name: 'Swedish, Sweden' },
      { code: 'no-NO', name: 'Norwegian, Norway' },
      { code: 'fi-FI', name: 'Finnish, Finland' },
      { code: 'da-DK', name: 'Danish, Denmark' },
      { code: 'he-IL', name: 'Hebrew, Israel' },
      { code: 'el-GR', name: 'Greek, Greece' },
      { code: 'hu-HU', name: 'Hungarian, Hungary' },
      { code: 'cs-CZ', name: 'Czech, Czech Republic' },
      { code: 'sk-SK', name: 'Slovak, Slovakia' },
      { code: 'uk-UA', name: 'Ukrainian, Ukraine' },
      { code: 'ro-RO', name: 'Romanian, Romania' },
      { code: 'bg-BG', name: 'Bulgarian, Bulgaria' },
      { code: 'sr-RS', name: 'Serbian, Serbia' },
      { code: 'hr-HR', name: 'Croatian, Croatia' },
      { code: 'sl-SI', name: 'Slovenian, Slovenia' },
      { code: 'lt-LT', name: 'Lithuanian, Lithuania' },
      { code: 'lv-LV', name: 'Latvian, Latvia' },
      { code: 'et-EE', name: 'Estonian, Estonia' },
      { code: 'is-IS', name: 'Icelandic, Iceland' },
      { code: 'fa-IR', name: 'Persian, Iran' },
      { code: 'ur-PK', name: 'Urdu, Pakistan' },
      { code: 'ta-IN', name: 'Tamil, India' },
      { code: 'te-IN', name: 'Telugu, India' },
      { code: 'kn-IN', name: 'Kannada, India' },
      { code: 'ml-IN', name: 'Malayalam, India' },
      { code: 'mr-IN', name: 'Marathi, India' },
      { code: 'gu-IN', name: 'Gujarati, India' },
      { code: 'pa-IN', name: 'Punjabi, India' },
      { code: 'am-ET', name: 'Amharic, Ethiopia' },
      { code: 'zu-ZA', name: 'Zulu, South Africa' },
      { code: 'xh-ZA', name: 'Xhosa, South Africa' },
      { code: 'af-ZA', name: 'Afrikaans, South Africa' },
      { code: 'id-ID', name: 'Indonesian, Indonesia' },
      { code: 'fil-PH', name: 'Filipino, Philippines' },
      { code: 'my-MM', name: 'Burmese, Myanmar' },
      { code: 'km-KH', name: 'Khmer, Cambodia' },
      { code: 'lo-LA', name: 'Lao, Laos' },
      { code: 'si-LK', name: 'Sinhala, Sri Lanka' },
      { code: 'mn-MN', name: 'Mongolian, Mongolia' },
      { code: 'ne-NP', name: 'Nepali, Nepal' },
      { code: 'ps-AF', name: 'Pashto, Afghanistan' },
      { code: 'kk-KZ', name: 'Kazakh, Kazakhstan' },
      { code: 'uz-UZ', name: 'Uzbek, Uzbekistan' },
      { code: 'ky-KG', name: 'Kyrgyz, Kyrgyzstan' },
      { code: 'tg-TJ', name: 'Tajik, Tajikistan' },
      { code: 'tk-TM', name: 'Turkmen, Turkmenistan' },
      { code: 'az-AZ', name: 'Azerbaijani, Azerbaijan' },
      { code: 'hy-AM', name: 'Armenian, Armenia' },
      { code: 'ka-GE', name: 'Georgian, Georgia' },
      { code: 'sq-AL', name: 'Albanian, Albania' },
      { code: 'bs-BA', name: 'Bosnian, Bosnia and Herzegovina' },
      { code: 'mk-MK', name: 'Macedonian, North Macedonia' },
      { code: 'mt-MT', name: 'Maltese, Malta' },
      { code: 'ga-IE', name: 'Irish, Ireland' },
      { code: 'cy-GB', name: 'Welsh, United Kingdom' },
      { code: 'gd-GB', name: 'Scottish Gaelic, United Kingdom' },
      { code: 'yi', name: 'Yiddish' },
      { code: 'ha-NG', name: 'Hausa, Nigeria' },
      { code: 'ig-NG', name: 'Igbo, Nigeria' },
      { code: 'yo-NG', name: 'Yoruba, Nigeria' },
      { code: 'so-SO', name: 'Somali, Somalia' },
      { code: 'ti-ER', name: 'Tigrinya, Eritrea' },
      { code: 'rw-RW', name: 'Kinyarwanda, Rwanda' },
      { code: 'ln-CD', name: 'Lingala, Congo' },
      { code: 'kg-CD', name: 'Kongo, Congo' },
      { code: 'sn-ZW', name: 'Shona, Zimbabwe' },
      { code: 'ny-MW', name: 'Chichewa, Malawi' },
      { code: 'st-ZA', name: 'Sesotho, South Africa' },
      { code: 'ts-ZA', name: 'Tsonga, South Africa' },
      { code: 'tn-ZA', name: 'Tswana, South Africa' },
      { code: 've-ZA', name: 'Venda, South Africa' },
      { code: 'ss-ZA', name: 'Swati, South Africa' },
      // Add more languages as needed
    ]
      .map((language) => language)
      .sort((a, b) => a.name.localeCompare(b.name));
  }
  private getEnvUrl(): string {
    let envUrl = 'http://localhost:3000'; // Default value
    this.http.get('env.json').subscribe((data) => {
      const apiUrl = (data as { BACKEND_URL: string })["BACKEND_URL"];
      if (apiUrl) {
        envUrl = apiUrl;
        this.apiUrl.next(envUrl); // Update the BehaviorSubject with the environment URL
      } else {
        console.error('API URL not found in env.json');
      }
    });
    return envUrl; // Ensure a string is returned
  }
}
