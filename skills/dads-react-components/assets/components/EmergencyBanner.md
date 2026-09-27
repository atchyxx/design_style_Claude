# EmergencyBanner

元のフォルダ: `src/components/EmergencyBanner/`。`scripts/add_components.py` で個別のファイルに展開できる。

<!-- file: EmergencyBanner.tsx -->
````tsx
import type { ComponentProps } from 'react';

export const bannerBodyStyle =
  'block px-2.5 py-3.5 border-[6px] bg-white desktop:p-[calc(26/16*1rem)] border-warning-orange-1';

type Props = ComponentProps<'div'>;

export const EmergencyBanner = (props: Props) => {
  const { className, children } = props;

  return <div className={`${bannerBodyStyle} ${className ?? ''}`}>{children}</div>;
};
````

<!-- file: index.ts -->
````ts
export { EmergencyBanner } from './EmergencyBanner';
export { EmergencyBannerBody } from './parts/Body';
export { EmergencyBannerButton } from './parts/Button';
export { EmergencyBannerHeading } from './parts/Heading';
````

<!-- file: parts/Body.tsx -->
````tsx
import type { ComponentProps } from 'react';

type Props = ComponentProps<'div'>;

export const EmergencyBannerBody = (props: Props) => {
  const { className, children } = props;

  return <div className={`mt-2 desktop:mt-4 ${className ?? ''}`}>{children}</div>;
};
````

<!-- file: parts/Button.tsx -->
````tsx
import type { ComponentProps } from 'react';

type Props = ComponentProps<'a'>;

export const EmergencyBannerButton = (props: Props) => {
  const { className, children, ...rest } = props;

  return (
    <a
      className={`
        relative block mx-auto p-[calc(18/16*1rem)] w-full border-2 border-transparent bg-error-1 text-white text-oln-16B-100 text-center rounded-12
        desktop:p-5 desktop:w-fit desktop:min-w-[50%] desktop:border-4 desktop:rounded-16
        after:absolute after:inset-0 after:border-2 after:border-white after:rounded-[calc(10/16*1rem)]
        desktop:after:border-4 desktop:after:rounded-12
        hover:underline hover:underline-offset-[calc(3/16*1rem)] hover:bg-error-2
        focus-visible:outline focus-visible:outline-[calc(4/16*1rem)] focus-visible:outline-black focus-visible:outline-offset-[calc(2/16*1rem)] focus-visible:ring-[calc(2/16*1rem)] focus-visible:ring-yellow-300
        ${className ?? ''}
      `}
      {...rest}
    >
      {children}
      {props.target === '_blank' && <NewWindowIcon className='ml-1 align-top' />}
    </a>
  );
};

type NewWindowIconProps = ComponentProps<'svg'>;

const NewWindowIcon = (props: NewWindowIconProps) => {
  const { className, ...rest } = props;

  return (
    <svg
      aria-label={`${rest['aria-label'] ?? '新規タブで開きます'}`}
      className={`inline ${className ?? ''}`}
      fill='none'
      height='16'
      role='img'
      viewBox='0 0 16 16'
      width='16'
    >
      <g>
        <path
          clipRule='evenodd'
          d='M3 13.5H13V9.16667H14V14.5H2V2.5H7.33333V3.5H3V13.5ZM9.33333 3.5V2.5H14V7.16667H13V4.23333L7 10.1667L6.33333 9.5L12.2667 3.5H9.33333Z'
          fillRule='evenodd'
          fill='currentColor'
        />
      </g>
    </svg>
  );
};
````

<!-- file: parts/Heading.tsx -->
````tsx
import type { ComponentProps } from 'react';

export type EmergencyBannerHeadingLevel = 'h2' | 'h3' | 'h4' | 'h5' | 'h6';

type EmergencyBannerHeadingProps = ComponentProps<'h2'> & {
  level: EmergencyBannerHeadingLevel;
};

export const EmergencyBannerHeading = (props: EmergencyBannerHeadingProps) => {
  const { level, className, children, ...rest } = props;
  const Tag = level;

  return (
    <Tag
      className={`
        text-std-20B-150 text-black desktop:text-std-24B-150
        ${className ?? ''}
      `}
      {...rest}
    >
      【緊急】
      {children}
    </Tag>
  );
};
````
