import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateUrlBarComponent } from './update-url-bar.component';

describe('UpdateUrlBarComponent', () => {
  let component: UpdateUrlBarComponent;
  let fixture: ComponentFixture<UpdateUrlBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UpdateUrlBarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UpdateUrlBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
