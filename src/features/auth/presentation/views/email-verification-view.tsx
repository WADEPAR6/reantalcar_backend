import { Suspense } from "react";
import { EmailVerificationComponent } from "../components/email-verification";

export const EmailVerificationView = () => {
    return (
        <div>
            <Suspense fallback={<div>Loading...</div>}>
                <EmailVerificationComponent />
            </Suspense>
        </div>
    );
};
