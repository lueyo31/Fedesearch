import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Result } from '../../models/result';

@Injectable({
  providedIn: 'root',
})
export class ModalService {
  private showSubject = new BehaviorSubject<boolean>(false);
  private resultSubject = new BehaviorSubject<Result>({
    id: 'example-id',
    link: 'https://example.com',
    linkPage: 'https://example.com/main',
    title: 'Example Title',
    description: 'This is an example description.',
    type: { name: 'web' },
    score: 4.5,
    motor: 'Example Engine',
  });

  show$ = this.showSubject.asObservable();
  result$ = this.resultSubject.asObservable();

  constructor() { }

  open(result: Result) {
    this.resultSubject.next(result);
    this.showSubject.next(true);
    console.log('Modal opened with result:', result);
  }

  close() {
    this.showSubject.next(false);
  }

  getResult(): Observable<Result> {
    return this.result$;
  }

  isModalOpen(): Observable<boolean> {
    return this.show$;
  }
}
