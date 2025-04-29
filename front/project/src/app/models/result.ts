import { Type } from "./type"
export interface Result {
  id: string; //UUID generated
  title: string; // map of title
  description: string; // map of content
  link: string; //URL map of url
  linkPage: string; //URL to the main page map of parsed URL https://{parsed_url[1]} or trim of url
  type: Type;
  score: number; //double map of score
  motor: string; //string map of engine

}
