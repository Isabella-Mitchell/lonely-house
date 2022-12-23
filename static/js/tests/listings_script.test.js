/**
 * @jest-environment jsdom
 */

jest.mock('../listings_script');

const $ = require('jquery');

const sum = require('../listings_script');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});