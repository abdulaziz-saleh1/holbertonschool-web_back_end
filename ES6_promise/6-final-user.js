import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) =>
    results.map((res) =>
      res.status === 'fulfilled'
        ? { status: res.status, value: res.value }
        : { status: res.status, value: String(res.reason) }
    )
  );
}
