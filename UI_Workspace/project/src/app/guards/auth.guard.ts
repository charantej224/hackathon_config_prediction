import { Injectable } from '@angular/core';
import { Router, CanActivate, RouterStateSnapshot, ActivatedRouteSnapshot } from '@angular/router';

@Injectable()
export class AuthGuard implements CanActivate {
    constructor(private router: Router) {

    }

    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        //if (this.authService.loggedIn() && state.url !== "/") {
        //    return true;
        //}
        //else if (this.authService.loggedIn() && state.url === "/") {
        //    this.router.navigate(['home']);
        //    return true;
        //}
        //else if (!this.authService.loggedIn() && state.url !== "/") {
        //    this.router.navigate(['/']);
        //    return false;
        //}
        //else if (state.url === "/") {
        //    return true;
        //}
        return true;
    }
}
